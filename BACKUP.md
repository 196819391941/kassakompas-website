# KassaKompas — volledige drietalige testwebsite

Volledige bronback-up van de private test-Site, gepubliceerd op 13 november 2026.

- Site: https://kassakompas-publicatietest-20261113.bluishcity.chatgpt.site
- Sites-versie: 10
- Gepubliceerde broncommit: `f4a197af59c3ced88d4080a6c09239212adda62f`
- Deployment: `appgdep_6af76a060a208191ab1cce1242fd958c`, geslaagd.
- 45 klantenpagina’s in Nederlands, Frans en Engels: 135 routes.
- Alle 289 bronbestanden, inclusief afbeeldingen, sectorpagina’s, webshop, vertaalwoordenboeken, generator, iconen, navigatie en hostingconfiguratie.
- Extra controlebestanden: dit document en `BACKUP-SHA256.json`.

De oorspronkelijke publieke website https://kassakompas-homepage-voorbeeld.bluishcity.chatgpt.site is niet gewijzigd door deze publicatie. De GitHub-hoofdbranch en de zichtbaarheidsinstellingen zijn niet aangepast. Deze afzonderlijke back-upbranch activeert geen GitHub Pages-publicatie vanaf main.

## Controle

De statische controle verifieert alle 135 routes, interne taalverwijzingen, assets inclusief responsive srcset en een herhaalbare generator. Browsercontrole: alle routes op 1440, 390 en 320 pixels, vaste navigatie, geen layout- of JavaScriptfouten. Na herstel van relatieve srcset-verwijzingen zijn alle betrokken foto’s opnieuw op drie breedtes gecontroleerd. De Franse en Engelse winkelmand, opties, aantallen, btw, besteloverzicht/download en aanvraagformulier zijn getest zonder een e-mail te verzenden. Prijscalculator, contactvenster en behoud van productselectie bij taalwissel zijn gecontroleerd.

De back-up wordt na aanmaak opnieuw van GitHub opgehaald. Elk bronbestand wordt op SHA-256 vergeleken met de gepubliceerde broncommit en, voor de deploymentbestanden, het gebruikte publicatiearchief. `BACKUP-SHA256.json` bevat de verwachte hashes.
