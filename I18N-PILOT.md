# KassaKompas — taalproef NL, FR en EN

Deze proef is uitsluitend gepubliceerd op het bestaande privétestproject. De oorspronkelijke openbare website, URL en toegangsinstellingen blijven behouden.

## Pagina’s

| Pagina | Nederlands | Frans | Engels |
| --- | --- | --- | --- |
| Homepage | `/index.html` | `/fr/` | `/en/` |
| Complete HAPOS-kassa | `/shop/hapos-compleet/` | `/fr/shop/caisse-hapos-complete/` | `/en/shop/complete-hapos-pos/` |

De taalkeuze werkt met gewone links en vereist geen JavaScript om de juiste pagina te openen. Nederlands is de standaard; er is geen automatische omleiding op basis van browsertaal. Bij wisselen blijven de pagina en het anker behouden. Op de productpagina blijven de uitvoering, het aantal en de gekozen extra licentie behouden wanneer JavaScript beschikbaar is. De winkelmand gebruikt dezelfde bestaande product-ID’s, opslag en prijsberekening.

## Vertalingen en grenzen

- Volledige zichtbare webtekst van beide proefpagina’s, navigatie, bijschriften, metadata en beschrijvende alt-teksten vertaald naar professioneel Frans en Engels.
- Productkeuzes, kostenregels en bevestigingsmeldingen worden ook vertaald. Valutabedragen gebruiken de notatie van de gekozen taal.
- Foto’s en de goedgekeurde Nederlandstalige software-interface in de productillustratie blijven intact. Dit is geen toezegging over de beschikbare talen van de kassasoftware.
- Overige pagina’s, waaronder het winkelmandje en bestellen, blijven voorlopig Nederlands. De melding bovenaan maakt dit duidelijk; de vertaalde winkelmandlinks vermelden NL.
- Geen productprijzen, product-ID’s, installatiekosten, garantietarieven of voorwaarden gewijzigd.
- Unieke paginatitels, beschrijvingen, taalattributen, canonieke test-URL’s en hreflang-varianten aangebracht. Bestaande noindex-instructies van de homepage behouden.

## Onderhoud

`locales/pilot.json` bevat de bronteksten en de Franse/Engelse vertalingen. `python scripts/build-language-pilot.py` bouwt de vier vertaalde HTML-pagina’s, taalkeuze en kleine clientwoordenlijst opnieuw op vanuit de Nederlandse proefpagina’s. De bouwstap is herhaalbaar en gebruikt alleen de standaardbibliotheek van Python. Geen nieuwe runtimebibliotheek of serverinfrastructuur.

De bestaande `dist/shop/shop.js` gebruikt vertaalfuncties alleen waar productbediening tekst genereert. Op Nederlandse en overige bestaande shoppagina’s blijven de oorspronkelijke teksten en valutaweergave behouden.
