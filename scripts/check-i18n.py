from pathlib import Path
from lxml import html
from urllib.parse import urlsplit,unquote
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1];D=R/'dist';routes=json.load(open(R/'locales/routes.json'));broken=[];cross=[]
def file(p):return D/(p.lstrip('/')+('index.html' if p.endswith('/') else ''))
for n,paths in routes.items():
 for lang,path in paths.items():
  doc=html.fromstring(file(path).read_text());assert doc.xpath('//html/@lang')[0].split('-')[0]==lang,(path,'lang')
  assert len(doc.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," language-switch ")]'))==1,(path,'switch')
  assert len(doc.xpath('//link[@rel="alternate"]'))==4
  assert not doc.xpath('//*[contains(@class,"language-pilot-note")]')
  for el in doc.xpath('//*[@href or @src or @poster or @srcset]'):
   for a in ['href','src','poster','srcset']:
    v=el.get(a)
    if a=='srcset' and v:
     for part in v.split(','):
      ref=urlsplit(part.strip().split()[0]);assert file(unquote(ref.path)).exists(),(path,part)
     continue
    if not v or not v.startswith('/'):continue
    u=urlsplit(v);target=file(unquote(u.path))
    if not target.exists():broken.append((path,v))
    if a=='href' and target.suffix=='.html' and el.get('hreflang') is None and lang!='nl' and u.path not in [x[lang] for x in routes.values()]:cross.append((path,v))
print('Routes',len(routes)*3,'Broken assets/links',sorted(set(broken)),'Wrong-language links',sorted(set(cross)))
assert not broken and not cross
before={str(p.relative_to(D)):hashlib.sha256(p.read_bytes()).hexdigest() for p in D.rglob('*') if p.is_file()}
subprocess.run(['python','scripts/build-i18n.py'],cwd=R,check=True,capture_output=True)
after={str(p.relative_to(D)):hashlib.sha256(p.read_bytes()).hexdigest() for p in D.rglob('*') if p.is_file()}
assert before==after,'Build not idempotent'
# Original product data and assets remain byte-for-byte unchanged.
for p in D.rglob('*'):
 if p.is_file() and (p.suffix not in ['.html','.js','.css','.json'] or p.name=='catalogue.js'):
  rel=str(p.relative_to(R));old=subprocess.run(['git','show','HEAD:'+rel],cwd=R,capture_output=True)
  if old.returncode==0:assert old.stdout==p.read_bytes(),rel
print('PASS static route, language, link, asset and repeatable-build audit')
