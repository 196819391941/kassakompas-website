# KassaKompas Shop

Eerste shopversie, 12 november 2026. Bestaande hosting en statische projectstructuur behouden. Shop staat na Prijzen op alle 24 bestaande pagina's met hoofdnavigatie. De oorspronkelijke pagina-inhoud is behouden; de extra navigatiestijl voorkomt afsnijden op tablets.

## Assortiment en prijsbron

Bron: https://www.onlinefact.be/shop/ en de door de gebruiker aangeleverde onlinefact.rar met afdrukken van de shop, bundels, PAX A77 en HAPOS. Nieuwe Nederlandstalige productteksten; geen overgenomen reviews, voorraadbeloftes of Onlinefact-merkvoering.

Alle productprijzen excl. btw. De gebruiker bevestigde: lifetime €1.400 voor retail en horeca; blackbox bij horeca inbegrepen mits €10 per maand lifetime garantie / blackboxverzekering; PAX A77 aankoop €495; Epson-bonprinter €149. De exact te leveren Epson-uitvoering wordt bevestigd, omdat de bron de €149-printer als DC-80250II benoemt en niet als specifiek Epson-model. Los touchscreen zonder klantendisplay: prijs op aanvraag totdat de gebruiker de afzonderlijke prijs bevestigt. Touchscreen + klantendisplay €879, slanke LCD-uitvoering €1.079. Geen €830 interne hardwaretoerekening als winkelprijs gebruikt.

Overige bronprijzen: bundel €1.095, premium €1.295, huur €85/maand, retaillicentie €29/maand of €248/jaar, extra licentie €10/maand, installatie €395, geldlade €89, rollen 80 mm (5) €8, Dibal D-POS 400 met ijking €499. Jaarhuur €840 (€70 per maand) en volledige HAPOS-aankoop €2.495 komen uit de goedgekeurde Prijzen-pagina. Bij de complete HAPOS-opstelling zijn lifetime kassalicentie en installatie al inbegrepen.

PAX: huur €36/maand met support en simkaart; aankoop toestel €495 met €12,90/maand support en simkaart. Beide hebben €45 eenmalige dossierkost, volgens de opgegeven bronformule. Dossierkost, eerste maand en daaropvolgende kosten zijn apart zichtbaar. Contractduur, transactietarieven, uitvoering en levering worden bevestigd.

## Bundelopties

Aankoopbundels: optionele maand-, jaar- of lifetime licentie, plus installatie €395. Huur: standaardsoftware blijft inbegrepen; optioneel extra licentie en installatie. Volledige HAPOS: lifetime en installatie blijven inbegrepen, alleen extra kassalicenties optioneel. De opties blijven aan hun bundel gekoppeld in het mandje; aantalwijzigingen schalen alle gekozen opties mee. Ongeldige of dubbele opties worden weggefilterd.

## Bestelverloop

Catalogus met zoekfunctie en categorieën, 17 productpagina's, winkelmandje en bestelgegevens. Alleen product-ID's, varianten, opties en aantallen worden in localStorage bewaard, geen persoonsgegevens. De winkelmand vertrouwt geen opgeslagen prijzen: alle bedragen worden opnieuw uit de catalogus afgeleid in gehele eurocenten. Aantallen 1–99. De eerste maand en/of het eerste jaar worden éénmaal bij de start opgeteld; vervolgkosten staan apart. Getoonde btw 21% is het Belgische standaardtarief; eventuele buitenlandse/afwijkende btw-behandeling wordt bij de aanvraag bevestigd.

Online betaling is niet aangesloten en wordt nergens als geslaagd voorgesteld. De huidige werkende afronding is een per e-mail te versturen bestelaanvraag met downloadbaar tekstoverzicht. Er wordt geen order op een server opgeslagen en geen orderbevestiging of levering voorgespiegeld. Afhalen op afspraak €0; eventuele verzendkosten en levertijd op bevestiging. Geen onbevestigde voorraadstatus, levertermijn of betaalproviderlogo's.

## Volgende stap: betalingen en domein

Een echte Mollie-koppeling vereist een serverendpoint dat de catalogusprijzen en beschikbaarheid zelf valideert, een order bewaart, een betaling aanmaakt en een ondertekende/geverifieerde providerstatus via webhook verwerkt. API-geheimen horen uitsluitend server-side. Maand-/jaarformules vereisen daarnaast bevestigde abonnementsvoorwaarden en de juiste terugkerende betaalmandaten. Niet simpelweg een actieve betaalknop op de huidige statische checkout zetten. Geen Mollie-account of domeininstellingen aangepast.

Voor betaalactivatie moeten ook bedrijfs-/btw-identificatie, leveringskosten, contractduur en de licentie/garantievoorwaarden definitief worden bevestigd. Het losse touchscreen heeft nog geen bevestigde winkelprijs.

## Verificatie

Browsercontroles: categorieën, zoeken, varianten, bundelopties, mandje, aantalwijzigingen, herladen, invoervalidatie, leveringskeuze, gegenereerde e-mail en downloadbaar overzicht. Tests onderscheppen de mailto-actie; er wordt geen e-mail verstuurd. Layout en zichtbaarheid van navigatie op 1440, 1024, 768, 390 en 320 pixels. Bestaande Prijzen-component met scherpe native SVG-interface hergebruikt in de HAPOS-beelden. Externe productfoto's komen uit de aangeleverde PDF's; software-/printerillustraties zijn als illustratie herkenbaar.

Een oude interne ChatGPT-bewerklink is uit de homepagebron verwijderd voordat de nieuwe volledige openbare back-up wordt gemaakt. De klantnavigatie en overige pagina-inhoud blijven behouden.

Na blokkering van de eerste back-uppoging is ook de volledige ongebruikte editor-composer (een opgeslagen, verborgen Sites-bewerkwerkbalk in een shadow-template) uit Home, Horeca en Retail verwijderd, samen met oude saved-from-URL-comments. Dit verwijdert uitsluitend tooling buiten de klantinhoud. Deze opgeschoonde bron wordt opnieuw gepubliceerd en exact geback-upt.

## Shop-productbeelden vernieuwd

Alle kassabundels en touchscreens tonen nu hetzelfde goedgekeurde transparante hardwarebeeld met de scherpe native SVG-fotoproducteninterface als Prijzen. Geen zwarte achtergrond of blauwe wolk. De precieze uitvoering/klantendisplay blijft in de beschrijving op bevestiging; het beeld is illustratief. Softwarelicenties tonen een gegenereerde KassaKompas-softwaredoos met bestaand merkbeeld en tekst “Retail of Horeca”; dit is een verpakkingsillustratie voor een digitale licentie, geen toezegging van fysieke verpakking. Ook de winkelmand gebruikt de nieuwe beelden.

PAX A77: de overzichtsminiatuur van 172×172 is vervangen door de grotere bronfoto van 582×495 uit de aangeleverde PAX-product-PDF (geëxtraheerd als 52.jpeg). Geen gegenereerde terminal, kunstmatige vergroting of verscherpingsfilter. Fabrikantbeelden zijn online gevonden op https://www.paxtechnology.com/a77 en https://www.pax.us/products/mobile/a77/; rechtstreekse download is door de omgevingsnetwerkregels geblokkeerd. De gebruikte lokale foto komt daarom uit de gebruikersbijlage.

Prijzen, varianten, licentie-/installatieopties en berekeningen zijn behouden.

## Bundels en accessoires samen afgebeeld

Op verzoek van 13 november staan bij de bundels de losse accessoires onder onze bestaande native kassa-interface in hetzelfde beeldkader. Complete HAPOS-aankoop €2.495: uitsluitend bonprinter en illustratieve blackbox naast de kassa; de blackbox is expliciet voor horeca aangeduid. Gewone en premium hardwarebundel: geldlade, scanner en bonprinter. Huurbundel: dezelfde accessoires plus de KassaKompas-softwaredoos als inbegrepen software. Hardware/klantendisplay: kleiner display voor standaarduitvoeringen, groter LCD-display voor premium/slanke LCD-uitvoering, achter de bestaande hoofdterminal gepositioneerd. Het hoofdtoestel, de scherpe fotoproducteninterface en de prijs-/optieberekeningen zijn behouden. De generieke blackbox en losse LCD-accessoire zijn illustratief gegenereerd; geen specifiek model of certificering wordt geclaimd door die afbeeldingen.

## Shop-afwerking en nieuwe producten — 13 november 2026

Blackbox kleiner dan printer in alle bundelbeelden; prijs bij hero staat apart onder het productbeeld en bedekt geen toestel. Geldlades worden expliciet afgebeeld en direct geladen in gewone, premium- en huurbundel. De huurbundel heeft een rustig blauw prijsaccent met stericoon (€85/maand, bij jaarselectie op de detailpagina €70/maand met toelichting). Geen onbevestigde populariteitsstatistiek geclaimd.

Retail maandlicentie heet nu Kassalicentie; bestaande product-ID en URL blijven behouden. Het voormalige losse scherm is op dezelfde URL/product-ID vervangen door een all-in-one toestel met ingebouwde bonprinter en klantendisplay voor €879 excl. btw, met softwarelicentie afzonderlijk. De all-in-one gebruikt exact de bestaande native KassaKompas/HAPOS-interface met 16 fotoproducten, geprojecteerd op het hardwarebeeld. Een Brother QL-600 labelprinter van €85 excl. btw is toegevoegd. Andere prijzen en opties zijn behouden.

Bij alle afgebeelde klantendisplays benoemt de productinformatie expliciet de aanwezigheid en plaatsing; bij premium/slanke LCD-uitvoering wordt het grotere LCD-klantenscherm aan de achterkant vermeld.

Nieuwe scherpe illustratieve productbeelden voor Epson-bonprinter, geldlade, vijf kassarollen, weegschaal en labelprinter zijn gegenereerd, waar beschikbaar op basis van de gebruikersbijlage. Illustratieve installatiefoto is eveneens gegenereerd en als illustratief benoemd. Geen foto van Over ons is gebruikt. Bij exacte modellen, aansluitingen, softwarekoppeling en uitvoering blijft voorafgaande bevestiging vereist. De foto’s zijn geen nieuwe compatibiliteits- of certificeringsclaims.

Bron assortiment/prijscontrole: https://www.onlinefact.be/shop/bundels/all-in-one-scherm-(touchscreen-printer-vfd-display)-871/ en https://www.onlinefact.be/shop/labelprinters/brother-ql-600-81/ . De all-in-one-prijs €879 en labelprinterprijs €85 zijn door de gebruiker expliciet opgegeven.

Correctie op expliciet verzoek: het all-in-one hardwaremodel is NIET gegenereerd. Het gebruikt de oorspronkelijke, ongewijzigde JPEG uit de gebruikersbijlage (32.jpeg, 172×172). Alleen de scherminhoud wordt vervangen door de bestaande scherpe native KassaKompas/HAPOS-interface. Het afgekeurde gegenereerde all-in-one hardwarebeeld is niet in de publicatie opgenomen. De beschikbare bronfoto is klein; er wordt geen hogere fotografische resolutie geclaimd.

Shopintro uitgebreid met originele commerciële tekst over retail of horeca, kopen of huren, hardware en ondersteuning.

Shopafwerking: commerciële introductie met betaalbaarheid, huur vanaf €85 excl. btw; printer, weegschaal, rollen en lade kleiner in overzicht, grote beelden behouden bij doorklikken. Weegschaal opnieuw vrijstaand op transparantie; andere drie bestaande beelden al transparant. Volwaardige POS-kassa’s meer nadruk dan compact all-in-one model.

Extra afwerking: accessoires verder verkleind (max. 125 px desktop / 85 px mobiel), grotere HAPOS-hardware, weegschaal opnieuw uitgesneden zonder vloer- of contactschaduw. Losse huurbadge verwijderd, ingetogen steraccent bij de bestaande huurprijs, ook op de detailpagina.

Publicatieherstel 13 november 2026: de gewijzigde Shop is visueel gecontroleerd en alle 182 deploymentbestanden komen overeen met broncommit d51d321705b4ebaf43b34d0cf94df606eb55a94d. Hosting publicatie faalt met “Failed to publish the built site”. Nieuw pakket gebruikt genormaliseerde USTAR-metadata; pagina’s en assets blijven bytegelijk aan de gecontroleerde versie.

Werkende privétest — Shopafwerking 13 november 2026: bovenste bonprinter en blackbox iets groter, alle losse klantendisplays apart rechtsonder bij de POS met bijschrift, maand- en jaarlicenties voor retail- of horecazaak, accessoires op tussenmaat en labelprinter in exact dezelfde verhouding. Alle 18 product-ID’s en prijzen behouden. Responsive gecontroleerd op 1440, 768, 390 en 320 px. Deze bron heeft de hostingidentiteit van het bestaande privétestproject; de oorspronkelijke openbare URL en publicatie zijn niet gewijzigd. Basis: volledige bron van oorspronkelijke Sites-versie 90.

Laatste detail: bundelbijschrift “Software” zonder “inbegrepen”; prijsblokken per rij gelijk uitgelijnd, inclusief het steraccent bij de huurprijs.

Extra afwerking: grote LCD-klantenschermen krijgen circa anderhalf keer de beeldhoogte van de gewone klantendisplays, ook mobiel en op detailpagina’s. Geldlade, kassarollen en weegschaal in het overzicht circa 15% groter; overige productbeelden en prijzen behouden.

Prijsaanpassing: losse lifetime kassalicentie voor retail of horeca van €1.400 naar €1.495 excl. btw. Overzicht, detailpagina, toelichtingen, catalogus en winkelmandberekening bijgewerkt. Hardwarebundels en maandelijkse blackboxverzekering ongewijzigd.

Laatste afwerking: Complete HAPOS-kassa krijgt hetzelfde prijsaccent met ster als de huurbundel, in overzicht en op productpagina. Labelprinter optisch gelijkgetrokken met de bonprinter door het verschil in afbeeldingsverhouding op te vangen. Prijzen en uitlijning behouden.

Taalproef: Nederlandse, Franse en Engelse homepage en Complete HAPOS-productpagina. Gewone taalkeuzelinks rechtsboven, behoud van pagina/anker en productselecties; overige pagina’s voorlopig Nederlands, zoals gemeld in de proef. Catalogus en prijzen ongewijzigd. Zie I18N-PILOT.md.
