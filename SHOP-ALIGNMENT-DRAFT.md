# Shopuitlijning — ongepubliceerd concept

Dit is een gerichte CSS-correctie op basis van de laatst bevestigde drietalige testwebsite (Sites-versie 10; broncommit f4a197af59c3ced88d4080a6c09239212adda62f; GitHub-back-up 312e8ae77afaae86b867bb81ec71869e6cf8a94d).

## Gewijzigd
- Alleen dist/shop/shop.css: gelijke beeldvakken, een identieke bovenpositie voor de POS-kassa's en een vaste accessoirezone met doorlopende scheidingslijn.
- Klantendisplays behouden hun bestaande grootteverschil en staan rechtsonder in dezelfde hoofdzone.
- De tekst onder de prijzen krijgt een gemeenschappelijke minimumhoogte, zodat prijsblokken en onderste scheidingslijnen gelijk staan binnen een productrij.
- De selectoren zijn beperkt tot .product-grid. Productdetailpagina's, prijzen, bestanden van hardwarefoto's, kassaschermopbouw, teksten en winkelmandlogica blijven intact.
- De gedeelde CSS geldt voor Nederlands, Frans en Engels.

## Nog niet uitgevoerd
De Cloud-werkruimte kon op 24 november 2026 niet opstarten: exec-server connection attempt failed / timed out recovering environment readiness from ERS.
Daarom is deze correctie NIET gepubliceerd en NIET visueel getest in een browser. De bestaande website blijft versie 10.
Voor publicatie zijn browsercontroles op 1440, 1024, 768, 560, 390 en 320 pixels nodig, in alle drie talen. Controleer POS-posities, accessoirelijntjes, lange labels, geen overlap/overflow, categoriefilters en werkende productlinks.

BACKUP.md en BACKUP-SHA256.json in de oorspronkelijke back-up beschrijven de ongewijzigde gepubliceerde versie 10. Deze conceptbranch is een afgeleide werkversie en geen geverifieerde nieuwe publicatie.
