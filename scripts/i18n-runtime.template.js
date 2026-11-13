/* Reviewed, local translations. Product IDs, customer input and software illustrations stay intact. */
(()=>{'use strict';const dictionaries=__TRANSLATIONS__,routes=__ROUTES__,language=document.documentElement.lang.split('-')[0],dict=dictionaries[language]||{},pairs=Object.entries(dict).filter(([a,b])=>a!==b&&a.length>4).sort((a,b)=>b[0].length-a[0].length);
function t(value){const raw=String(value),key=raw.trim().replace(/\s+/g,' ');if(dict[key])return raw.slice(0,raw.length-raw.trimStart().length)+dict[key]+raw.slice(raw.trimEnd().length);let result=raw;for(const [a,b] of pairs)if(result.includes(a))result=result.split(a).join(b);return result;}
function url(value){try{const u=new URL(value,location.href);if(u.origin!==location.origin)return value;for(const paths of Object.values(routes)){if(Object.values(paths).some(p=>u.pathname===p||p.endsWith('/')&&u.pathname===p+'index.html')||paths.nl==='/'&&u.pathname==='/index.html'){u.pathname=paths[language]||paths.nl;return u.pathname+u.search+u.hash;}}return value;}catch{return value;}}
function money(cents,fallback){return language==='nl'?fallback(cents):new Intl.NumberFormat(language==='fr'?'fr-BE':'en-IE',{style:'currency',currency:'EUR'}).format(cents/100);}
function translate(root){if(!root||root.nodeType===3&&root.parentElement?.closest('script,style,svg,textarea,[contenteditable],.register-display,.language-switch'))return;
 if(root.nodeType===3){const next=t(root.data);if(next!==root.data)root.data=next;return;}
 if(root.nodeType!==1&&root.nodeType!==9)return;if(root.matches?.('script,style,svg,textarea,[contenteditable],.register-display,.language-switch'))return;
 if(root.nodeType===1){for(const key of ['aria-label','title','placeholder','alt'])if(root.hasAttribute(key)){const old=root.getAttribute(key),next=t(old);if(old!==next)root.setAttribute(key,next);}for(const key of ['href','action'])if(root.hasAttribute(key)){const old=root.getAttribute(key),next=url(old);if(old!==next)root.setAttribute(key,next);}}
 for(const child of [...root.childNodes])translate(child);
}
window.KassaKompasI18n={t,url,money,language,translate};
function init(){// Observe only new dynamic UI; statically rendered copy is already translated.
 const observer=new MutationObserver(records=>{for(const r of records){if(r.type==='childList')for(const n of r.addedNodes)translate(n);else if(r.type==='characterData')translate(r.target);else if(r.type==='attributes'&&!r.target.closest('.language-switch')){const old=r.target.getAttribute(r.attributeName),next=r.attributeName==='src'?url(old):url(old);if(old!==next)r.target.setAttribute(r.attributeName,next);}}});observer.observe(document.body,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:['href','action','src']});
 document.querySelectorAll('.language-switch a').forEach(a=>a.addEventListener('click',()=>{const u=new URL(a.href,location.origin);u.hash=location.hash;u.search=location.search;const form=document.querySelector('#product-form');if(form){u.searchParams.set('variant',form.elements.variant.value);u.searchParams.set('quantity',form.elements.quantity.value);const license=form.querySelector('#bundle-license')?.value;if(license)u.searchParams.set('license',license);if(form.querySelector('#bundle-installation')?.checked)u.searchParams.set('installation','1');}a.href=u.href;}));
}
init();
})();
