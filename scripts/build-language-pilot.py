from pathlib import Path
from html.parser import HTMLParser
from html import escape,unescape
from urllib.parse import urljoin,urlsplit,urlunsplit
import json,re
ROOT=Path(__file__).resolve().parents[1];DIST=ROOT/'dist'
TRANSLATIONS=json.loads((ROOT/'locales/pilot.json').read_text())
ORIGIN='https://kassakompas-publicatietest-20261113.bluishcity.chatgpt.site'
PAGES={'home':{'nl':'/index.html','fr':'/fr/','en':'/en/'},'hapos':{'nl':'/shop/hapos-compleet/','fr':'/fr/shop/caisse-hapos-complete/','en':'/en/shop/complete-hapos-pos/'}}
LOCALES={'nl':'nl-BE','fr':'fr-BE','en':'en'}
EXEMPT={'KassaKompas','Kassa','Kompas','Cooking Corner','Joachim Verbrugge','’t Oud Scheepken','Walter van de Winkel','Timoda','0472 60 57 58','sales@kassakompas.com','Mispelstraat 107','9100 Sint-Niklaas','→','✓','+','/','0','€ 2.495,00'}
missing=set()
def text(value,lang):
 if lang=='nl':return value
 key=' '.join(value.split());mapping=TRANSLATIONS[lang]
 if not key:return value
 if key in mapping:return value[:len(value)-len(value.lstrip())]+mapping[key]+value[len(value.rstrip()):]
 # Composite accessible labels and metadata reuse the same reviewed phrases.
 result=key
 for a,b in sorted(mapping.items(),key=lambda x:len(x[0]),reverse=True):
  if len(a)>7:result=result.replace(a,b)
 if result==key and key not in EXEMPT and not re.fullmatch(r'[\d\s€.,/+−—]+',key):missing.add(key)
 return value[:len(value)-len(value.lstrip())]+result+value[len(value.rstrip()):]
def localized_url(value,base,lang):
 if not value or value.startswith(('#','data:','mailto:','tel:','javascript:','https:','http:','//')):return value
 u=urlsplit(urljoin(base,value));path=u.path
 for paths in PAGES.values():
  if path in {paths['nl'],'/' if paths['nl']=='/index.html' else paths['nl']+'index.html'}:path=paths[lang];break
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
   elif key in {'alt','title','placeholder','aria-label'} or (tag=='meta' and a.get('name')=='description' and key=='content'):new=text(value,self.lang)
   elif tag=='link' and a.get('rel')=='canonical' and key=='href':new=ORIGIN+PAGES[self.page][self.lang]
   elif key in {'href','src','data-target','action'}:new=localized_url(value,self.base,self.lang)
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
      if isinstance(v,dict):return {k:(ORIGIN+PAGES[self.page][self.lang] if k=='url' else walk(x)) for k,x in v.items()}
      if isinstance(v,list):return [walk(x) for x in v]
      if isinstance(v,str) and not v.startswith(('http:','https:')):return text(v,self.lang)
      return v
     d=json.dumps(walk(json.loads(d)),ensure_ascii=False)
    except json.JSONDecodeError:pass
   self.out.append(d)
  elif 'style' in self.stack:self.out.append(d)
  elif 'svg' in self.stack:self.out.append(escape(d,quote=False))
  else:self.out.append(escape(text(d,self.lang),quote=False))
def strip_pilot(source):return re.sub(r'<!--language-pilot-(head|switch|note)-->.*?<!--/language-pilot-\1-->','',source,flags=re.S)
def switch(page,lang):
 labels={'nl':'Nederlands','fr':'Français','en':'English'}
 return '<!--language-pilot-switch--><nav class="language-switch" aria-label="Taal / Langue / Language">'+''.join('<a href="'+PAGES[page][code]+'" lang="'+code+'" hreflang="'+LOCALES[code]+'" aria-label="'+label+'"'+(' aria-current="true"' if code==lang else '')+'>'+code.upper()+'</a>' for code,label in labels.items())+'</nav><!--/language-pilot-switch-->'
notes={
 'nl':('Taalproef','Homepage en Complete HAPOS-kassa zijn beschikbaar in drie talen. De overige pagina’s zijn nog Nederlands.','Homepage','Complete HAPOS-kassa'),
 'fr':('Aperçu multilingue','L’accueil et la caisse HAPOS complète sont disponibles en trois langues. Les autres pages sont encore en néerlandais.','Accueil','Caisse HAPOS complète'),
 'en':('Language preview','The homepage and Complete HAPOS POS page are available in three languages. Other pages are still in Dutch.','Home','Complete HAPOS POS')}
for page,paths in PAGES.items():
 basepath=DIST/(paths['nl'].lstrip('/')+('index.html' if paths['nl'].endswith('/') else ''))
 source=re.sub(r'\sdata-language-page="[^"]*"','',strip_pilot(basepath.read_text()))
 for lang,path in paths.items():
  rendered=''.join(Translator(source,page,lang).out)
  rendered=re.sub(r'<html\b([^>]*)>',lambda m:'<html'+m.group(1)+' data-language-page="'+page+'">',rendered,count=1)
  head='<!--language-pilot-head--><link rel="stylesheet" href="/language-pilot.css"><script type="module" src="/language-pilot.js"></script>'
  if 'rel="canonical"' not in rendered:head+='<link rel="canonical" href="'+ORIGIN+path+'">'
  head+=''.join('<link rel="alternate" hreflang="'+LOCALES[c]+'" href="'+ORIGIN+p+'">' for c,p in paths.items())+'<link rel="alternate" hreflang="x-default" href="'+ORIGIN+paths['nl']+'"><!--/language-pilot-head-->'
  rendered=rendered.replace('</head>',head+'</head>',1)
  def add_switch(m):return m.group().replace('</div></header>',switch(page,lang)+'</div></header>')
  rendered=re.sub(r'<header\b.*?</header>',add_switch,rendered,count=1,flags=re.S)
  title,body,home,product=notes[lang]
  note='<!--language-pilot-note--><aside class="language-pilot-note"><div class="wrap"><span><strong>'+title+'.</strong> '+body+'</span><span class="pilot-page-links"><a href="'+PAGES['home'][lang]+'">'+home+'</a><span aria-hidden="true">·</span><a href="'+PAGES['hapos'][lang]+'">'+product+'</a></span></div></aside><!--/language-pilot-note-->'
  rendered=rendered.replace('</header>','</header>'+note,1)
  target=DIST/(path.lstrip('/')+('index.html' if path.endswith('/') else ''));target.parent.mkdir(parents=True,exist_ok=True);target.write_text(rendered)
# Keep client translations small: only strings generated by the existing product controls.
dynamic=['Complete HAPOS-kassa','Extra kassalicentie','Eenmalig','Per maand','Per jaar, ineens','Per jaar','eenmalig','per maand','per jaar, ineens','Maak je bundel compleet','De standaardsoftware van deze bundel blijft inbegrepen. Kies hieronder eventueel een extra licentie.','Kies de gewenste softwarelicentie en eventueel installatie.','Extra licentie','Softwarelicentie','Geen extra licentie','Geen licentie toevoegen','Installatie en instructie zijn al inbegrepen.','FDM 2.0-blackbox inbegrepen bij horeca. Lifetime garantie / blackboxverzekering: €10 per maand. Support 24/7 in regie.','Bundel bij start:','excl. btw per opstelling','toegevoegd aan je winkelmandje.','Opslag is geblokkeerd: houd deze pagina open.','Bekijk je winkelmandje →','eenmalig excl. btw',' / maand',' / jaar']
translations={lang:{k:TRANSLATIONS[lang][' '.join(k.split())] for k in dynamic} for lang in ['fr','en']}
js='const translations='+json.dumps(translations,ensure_ascii=False)+';\n'+'''export const language=document.documentElement.lang.split('-')[0];
export function t(value){const raw=String(value),dict=translations[language];if(!dict)return raw;const key=raw.trim().replace(/\\s+/g,' ');if(dict[key])return raw.slice(0,raw.length-raw.trimStart().length)+dict[key]+raw.slice(raw.trimEnd().length);let result=raw;for(const [a,b] of Object.entries(dict).sort((x,y)=>y[0].length-x[0].length)){if(a.length>5)result=result.split(a).join(b);}return result;}
export function localizedMoney(cents,fallback){return language==='nl'?fallback(cents):new Intl.NumberFormat(language==='fr'?'fr-BE':'en-IE',{style:'currency',currency:'EUR'}).format(cents/100);}
function initLanguageSwitch(){document.querySelectorAll('.language-switch a').forEach(a=>a.addEventListener('click',()=>{const url=new URL(a.href,location.origin);url.hash=location.hash;const form=document.querySelector('#product-form');if(form){url.searchParams.set('variant',form.elements.variant.value);const n=Number(form.elements.quantity.value);if(n>1)url.searchParams.set('quantity',String(n));const license=form.querySelector('#bundle-license')?.value;if(license)url.searchParams.set('license',license);}a.href=url.href;}));}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',initLanguageSwitch,{once:true});else initLanguageSwitch();
'''
(DIST/'language-pilot.js').write_text(js)
print('Unmapped strings for review:',json.dumps(sorted(missing),ensure_ascii=False))
