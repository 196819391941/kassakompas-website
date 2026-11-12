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
