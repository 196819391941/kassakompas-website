from pathlib import Path
from html.parser import HTMLParser
from html import escape,unescape
from urllib.parse import urljoin,urlsplit,urlunsplit
import json,re
ROOT=Path(__file__).resolve().parents[1];DIST=ROOT/'dist'
TRANSLATIONS=json.loads((ROOT/'locales/site.json').read_text())
ORIGIN='https://kassakompas-publicatietest-20261113.bluishcity.chatgpt.site'
PAGES=json.loads((ROOT/'locales/routes.json').read_text())
LOCALES={'nl':'nl-BE','fr':'fr-BE','en':'en'}
EXEMPT={'KassaKompas','Kassa','Kompas','Cooking Corner','Joachim Verbrugge','’t Oud Scheepken','Walter van de Winkel','Timoda','0472 60 57 58','sales@kassakompas.com','Mispelstraat 107','9100 Sint-Niklaas','→','✓','+','/','0','€ 2.495,00','›','↓','↗'}
missing=set()
def text(value,lang):
 if lang=='nl':return value
 key=' '.join(value.split());mapping=TRANSLATIONS[lang]
 if not key:return value
 if key in mapping:return value[:len(value)-len(value.lstrip())]+mapping[key]+value[len(value.rstrip()):]
 if key not in EXEMPT and not re.fullmatch(r'[\d\s€.,/+−—%:()×·]+',key):missing.add(key)
 return value
def localized_url(value,base,lang):
 if not value or value.startswith(('#','data:','mailto:','tel:','javascript:','https:','http:','//')):return value
 u=urlsplit(urljoin(base,value));path=u.path
 for paths in PAGES.values():
  if path in set(paths.values()) | {p+'index.html' for p in paths.values() if p.endswith('/')} | ({'/index.html'} if paths['nl']=='/' else set()):path=paths[lang];break
 return urlunsplit(('','',path,u.query,u.fragment))
class Translator(HTMLParser):
 def __init__(self,source,page,lang):
  super().__init__(convert_charrefs=True);self.out=[];self.stack=[];self.page=page;self.lang=lang;self.base=PAGES[page]['nl'];self.script_type='';self.feed(source);self.close()
 def handle_decl(self,d):self.out.append('<!'+d+'>')
 def handle_comment(self,d):self.out.append('<!--'+d+'-->')
 def handle_startendtag(self,tag,attrs):self.handle_starttag(tag,attrs,True)
 def handle_starttag(self,tag,attrs,selfclosed=False):
  raw=self.get_starttag_text();a=dict(attrs)
  for key,value in attrs:
   if value is None:continue
   new=value
   if tag=='html' and key=='lang':new=LOCALES[self.lang]
   elif key in {'alt','title','placeholder','aria-label','data-request'} or (tag=='meta' and (a.get('name') in {'description','twitter:title','twitter:description'} or a.get('property') in {'og:title','og:description'}) and key=='content'):new=text(value,self.lang)
   elif tag=='meta' and a.get('property')=='og:locale' and key=='content':new={'nl':'nl_BE','fr':'fr_BE','en':'en_GB'}[self.lang]
   elif tag=='link' and a.get('rel')=='canonical' and key=='href':new=ORIGIN+PAGES[self.page][self.lang]
   elif key=='srcset':new=', '.join(' '.join([localized_url(part.strip().split()[0],self.base,self.lang)]+part.strip().split()[1:]) for part in value.split(','))
   elif key in {'href','src','data-target','action','poster'}:new=localized_url(value,self.base,self.lang)
   if new!=value:
    pattern=r'(\b'+re.escape(key)+r'\s*=\s*)([\"\']).*?\2'
    raw=re.sub(pattern,lambda m:m.group(1)+'"'+escape(new,quote=True)+'"',raw,count=1,flags=re.S|re.I)
  self.out.append(raw)
  if tag=='script':self.script_type=a.get('type','')
  if not selfclosed and tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append(tag)
 def handle_endtag(self,tag):
  self.out.append('</'+tag+'>')
  if tag in self.stack:
   while self.stack:
    if self.stack.pop()==tag:break
 def handle_data(self,d):
  if 'script' in self.stack:
   if self.script_type=='application/ld+json':
    try:
     def walk(v):
      if isinstance(v,dict):return {k:((LOCALES[self.lang] if k=='inLanguage' else x) if k.startswith('@') or k=='inLanguage' else (ORIGIN+localized_url(x.removeprefix(ORIGIN),self.base,self.lang) if k=='url' and isinstance(x,str) and x.startswith(ORIGIN) else walk(x))) for k,x in v.items()}
      if isinstance(v,list):return [walk(x) for x in v]
      if isinstance(v,str) and not v.startswith(('http:','https:')):return text(v,self.lang)
      return v
     d=json.dumps(walk(json.loads(d)),ensure_ascii=False)
    except json.JSONDecodeError:pass
   self.out.append(localize_script(d,self.lang) if self.script_type!='application/ld+json' else d)
  elif 'style' in self.stack:self.out.append(d)
  elif 'svg' in self.stack:self.out.append(escape(d,quote=False))
  else:self.out.append(escape(text(d,self.lang),quote=False))
def strip_pilot(source):return re.sub(r'<!--language-pilot-(head|switch|note)-->.*?<!--/language-pilot-\1-->','',source,flags=re.S)
def switch(page,lang):
 labels={'nl':'Nederlands','fr':'Français','en':'English'}
 return '<!--language-pilot-switch--><nav class="language-switch notranslate" translate="no" aria-label="Taal / Langue / Language">'+''.join('<a class="notranslate" translate="no" href="'+PAGES[page][code]+'" lang="'+code+'" hreflang="'+LOCALES[code]+'" aria-label="'+label+'"'+(' aria-current="true"' if code==lang else '')+'>'+code.upper()+'</a>' for code,label in labels.items())+'</nav><!--/language-pilot-switch-->'

def localize_script(code,lang):
 if lang=='nl':return code
 # Translate only reviewed literal strings, never selectors, field names or customer data.
 mapping=TRANSLATIONS[lang]
 pattern=r"('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")"
 def convert(m):
  token=m.group(); value=token[1:-1]; key=' '.join(value.split())
  if value.startswith('/contact/') or value.startswith('/shop/'):return json.dumps(localized_url(value,'/',lang),ensure_ascii=False)
  if value=='nl-BE':return json.dumps(LOCALES[lang])
  if key in mapping and (len(key)>4 or key in {'Voor'}):return json.dumps(value[:len(value)-len(value.lstrip())]+mapping[key]+value[len(value.rstrip()):],ensure_ascii=False)
  return token
 return re.sub(pattern,convert,code)
for page,paths in PAGES.items():
 basepath=DIST/(paths['nl'].lstrip('/')+('index.html' if paths['nl'].endswith('/') else ''))
 source=re.sub(r'\sdata-language-page="[^"]*"','',strip_pilot(basepath.read_text()))
 # Saved browser challenge is a stale capture artefact, not part of the website.
 source=re.sub(r'<script\b[^>]*>[^<]*?__CF\$cv\$params.*?</script>','',source,flags=re.S)
 for lang,path in paths.items():
  rendered=''.join(Translator(source,page,lang).out)
  rendered=re.sub(r'<html\b([^>]*)>',lambda m:'<html'+re.sub(r'\stranslate="[^"]*"','',m.group(1))+' data-language-page="'+page+'" translate="no">',rendered,count=1)
  head='<!--language-pilot-head--><meta name="google" content="notranslate"><link rel="stylesheet" href="/language-pilot.css"><script type="module" src="/language-pilot.js"></script>'
  if 'rel="canonical"' not in rendered:head+='<link rel="canonical" href="'+ORIGIN+path+'">'
  head+=''.join('<link rel="alternate" hreflang="'+LOCALES[c]+'" href="'+ORIGIN+p+'">' for c,p in paths.items())+'<link rel="alternate" hreflang="x-default" href="'+ORIGIN+paths['nl']+'"><!--/language-pilot-head-->'
  rendered=rendered.replace('</head>',head+'</head>',1)
  def add_switch(m):
   header=m.group();pos=header.rfind('</div>')
   return header[:pos]+switch(page,lang)+header[pos:]
  rendered=re.sub(r'<header\b.*?</header>',add_switch,rendered,count=1,flags=re.S)
  target=DIST/(path.lstrip('/')+('index.html' if path.endswith('/') else ''));target.parent.mkdir(parents=True,exist_ok=True);target.write_text(rendered)
(DIST/'i18n-routes.json').write_text(json.dumps(PAGES,ensure_ascii=False,separators=(',',':')))
# Shared, same-origin dictionary; no external translation services or dependencies.
dynamic_sources=' '.join((DIST/p).read_text() for p in ['shop/shop.js','shop/catalogue.js','prijzen/index.html','contact/index.html','horeca.html'])
client_translations={lang:{k:v for k,v in words.items() if k in dynamic_sources or len(k)<45} for lang,words in TRANSLATIONS.items()}
runtime=(ROOT/'scripts/i18n-runtime.template.js').read_text().replace('__TRANSLATIONS__',json.dumps(client_translations,ensure_ascii=False,separators=(',',':'))).replace('__ROUTES__',json.dumps(PAGES,separators=(',',':')))
(DIST/'i18n-runtime.js').write_text(runtime)
(DIST/'language-pilot.js').write_text("import '/i18n-runtime.js';\nexport const language=document.documentElement.lang.split('-')[0];\nexport const t=value=>window.KassaKompasI18n.t(value);\nexport const localizedMoney=(cents,fallback)=>window.KassaKompasI18n.money(cents,fallback);\nexport const localizedUrl=value=>window.KassaKompasI18n.url(value);\n")
print('Unmapped strings for review:',json.dumps(sorted(missing),ensure_ascii=False))
