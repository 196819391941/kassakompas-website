import {products} from './catalogue.js';
export const catalogue=products;
export const VAT=21;
export const money=cents=>new Intl.NumberFormat('nl-BE',{style:'currency',currency:'EUR'}).format(cents/100);
export function bundleOptions(id){
 if(['kassabundel','premium-kassabundel'].includes(id))return {installation:true,extra:false,licenses:[['retail-maandlicentie','maand'],['retail-jaarlicentie','jaar'],['lifetime-licentie','retail'],['lifetime-licentie','horeca']]};
 if(id==='huur-kassabundel')return {installation:true,extra:true,licenses:[['extra-kassalicentie','maand'],['extra-kassalicentie','jaar'],['lifetime-licentie','retail'],['lifetime-licentie','horeca']]};
 if(id==='hapos-compleet')return {installation:false,extra:true,licenses:[['extra-kassalicentie','maand'],['extra-kassalicentie','jaar']]};
 return null;
}
function validAddons(product,addons){const options=bundleOptions(product);if(!options||!Array.isArray(addons))return [];const allowed=options.licenses.concat(options.installation?[['installatie','eenmalig']]:[]),seen=new Set();let license=false;
 return addons.filter(a=>{if(!a||!allowed.some(([p,v])=>a.product===p&&a.variant===v)||seen.has(a.product))return false;if(a.product!=='installatie'){if(license)return false;license=true;}seen.add(a.product);return true;}).map(a=>({product:a.product,variant:a.variant})).sort((a,b)=>a.product.localeCompare(b.product));
}
export function cartKey(row){return row.product+':'+row.variant+':'+(row.addons||[]).map(a=>a.product+'/'+a.variant).join(',');}
export function cleanCart(value){if(!Array.isArray(value))return [];const valid=new Map();for(const row of value.slice(0,200)){if(!row||typeof row!=='object')continue;const p=products.find(p=>p.id===row.product),v=p?.variants.find(v=>v.id===row.variant);if(!v||!Number.isInteger(row.quantity)||row.quantity<1||row.quantity>99)continue;const item={product:p.id,variant:v.id,quantity:row.quantity,addons:validAddons(p.id,row.addons)},key=cartKey(item),prior=valid.get(key);item.quantity=Math.min(99,row.quantity+(prior?.quantity||0));valid.set(key,item);}return [...valid.values()];}
export function lines(cart){return cleanCart(cart).map(row=>{const product=products.find(p=>p.id===row.product),base=product.variants.find(v=>v.id===row.variant),addons=row.addons.map(a=>{const p=products.find(p=>p.id===a.product);return {product:p,variant:p.variants.find(v=>v.id===a.variant)};}),v={...base};for(const a of addons){v.once+=a.variant.once;v.month+=a.variant.month;v.year+=a.variant.year;}v.notes=[base.notes,...addons.map(a=>a.product.name+' — '+a.variant.label+(a.variant.notes?': '+a.variant.notes:''))].filter(Boolean).join(' · ');return {...row,productInfo:product,baseVariantInfo:base,variantInfo:v,addonsInfo:addons,key:cartKey(row)};});}
export function totals(cart){const t=lines(cart).reduce((t,r)=>{t.once+=r.variantInfo.once*r.quantity;t.month+=r.variantInfo.month*r.quantity;t.year+=r.variantInfo.year*r.quantity;return t;},{once:0,month:0,year:0});t.net=t.once+t.month+t.year;t.vat=Math.round(t.net*VAT/100);t.gross=t.net+t.vat;return t;}
