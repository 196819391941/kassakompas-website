import '/i18n-runtime.js';
export const language=document.documentElement.lang.split('-')[0];
export const t=value=>window.KassaKompasI18n.t(value);
export const localizedMoney=(cents,fallback)=>window.KassaKompasI18n.money(cents,fallback);
export const localizedUrl=value=>window.KassaKompasI18n.url(value);
