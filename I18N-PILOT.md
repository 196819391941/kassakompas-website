# KassaKompas — volledige meertalige website

De oorspronkelijke taalproef is uitgebreid tot alle 45 klantenpagina’s: Nederlands, Frans en Engels (135 routes). Nederlands blijft de standaard. De bestaande publieke oorspronkelijke Site is niet gewijzigd; deze uitwerking hoort bij de afzonderlijke, private test-Site in `.openai/hosting.json`.

## Bron en opbouw

- `locales/site.json`: handmatig uitgewerkte Franse en Engelse vertalingen met de oorspronkelijke Nederlandse tekst als sleutel.
- `locales/routes.json`: expliciete koppeling tussen de 45 pagina’s en hun drie URL’s.
- `scripts/build-i18n.py`: statische generatie van pagina’s, SEO-metadata, canonical- en hreflangverwijzingen. `build-language-pilot.py` blijft een compatibele ingang voor dezelfde volledige generatie.
- `scripts/i18n-runtime.template.js`: lichte gedeelde browserlogica voor dynamische winkel- en formulierteksten. Alleen dynamisch benodigde vertalingen komen in het browserbestand.
- Bestaande foto’s, hardwarebeelden en kassasoftwarebeelden zijn behouden. De voorbeeldsoftware op productafbeeldingen wordt niet vertaald en vormt geen belofte over ondersteunde softwaretalen.

Bewerken: wijzig Nederlandse bronpagina’s en voeg de bijbehorende teksten toe aan `locales/site.json`; voer daarna `python scripts/build-i18n.py` uit. De generator rapporteert onbekende teksten ter beoordeling. Pijlsymbolen zijn taalneutraal. Alle artikelteksten en metadata staan direct in de HTML: geen externe vertaalservice of nieuwe bibliotheek.

## Gedrag

De taalkeuze verwijst naar dezelfde pagina in de gekozen taal. Productvariant, aantal, extra licentie, installatiekeuze en URL-fragment blijven behouden. Productcodes, winkelmandopslag, prijzen en btw-berekeningen zijn gedeeld; er worden geen aparte taalproducten gemaakt. Klantinvoer wordt ongewijzigd verwerkt. De bestaande e-mailaanvraag blijft een aanvraag, geen online betaling.

HTML en taalkeuze zijn beschermd tegen automatische browservertaling (`translate="no"` en Google `notranslate`), zodat taalnamen niet veranderen en geen automatische omleiding ontstaat.

## Controle en publicatie

Controleer voor publicatie alle 135 routes, lokale assets, interne taalverwijzingen, herhaalbaarheid van de generator, responsive weergave en vaste navigatie. Test daarnaast productopties, winkelmandje, btw, prijscalculator, aanvraagformulier en besteloverzicht. Publiceer uitsluitend naar de bevestigde private test-Site. Maak daarna volgens `AGENTS.md` een volledige afzonderlijke GitHub-back-up en vergelijk alle bestanden opnieuw met SHA-256.
