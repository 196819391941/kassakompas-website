# Integratie en testverslag KassaKompas

Datum: 3 november 2026

## Toegevoegde pagina’s

| Aangeleverd bestand | Projectbestand |
| --- | --- |
| kassakompas-home-v8-navigatie.html | index.html |
| kassakompas-horeca-v8-navigatie.html | horeca.html |
| kassakompas-retail-v2-iconen.html | retail.html |

Teksten, kleuren, afbeeldingen, iconen en bestaande desktoplay-out zijn behouden. Afbeeldingen en iconen zijn ingebed in de HTML; er zijn geen losse afbeeldingsbestanden nodig.

## Gerichte correcties

- Links naar de aangeleverde bestandsnamen verwijzen nu naar index.html, horeca.html en retail.html.
- De twee klikbare sectorkaarten op de homepage verwezen in hun muis- en toetsenbordhandlers naar ontbrekende oudere HTML-bestanden. Die verwijzen nu naar retail.html en horeca.html.
- Op de homepage blijven alle paginalinks zichtbaar op smartphones; de navigatie mag naar een volgende regel doorlopen.
- Op horeca.html staan functiekaarten op smartphones in één kolom om horizontale overloop te voorkomen.
- Op retail.html staan sectorkaarten bij schermen tot 360 pixels breed in één kolom om overloop te voorkomen.

## Uitgevoerde tests

Lokale Chromium-browsertests via een server die uitsluitend op 127.0.0.1 luistert. Dit is geen openbare publicatie.

- Alle drie pagina’s getest op 1440 × 900, 768 × 1024, 390 × 844 en 320 × 720 pixels.
- Op alle twaalf combinaties: pagina geladen, afbeeldingen inclusief lazy-loaded afbeeldingen gedecodeerd, CSS-achtergrondafbeeldingen geladen, lokale ankerdoelen aanwezig en geen JavaScript-fouten.
- Na de mobiele correcties geen horizontale documentoverloop. De opzettelijk buiten beeld geplaatste toegankelijkheidslink op retail.html is geen overloopfout.
- Alle primaire paginalinks zichtbaar op de geteste schermbreedtes.
- 48 aanvullende interactietests geslaagd: navigatie tussen alle pagina’s, en beide homepagekaarten met muis, Enter en spatie op alle vier breedtes.
- Screenshots van alle twaalf combinaties gemaakt; desktop- en smartphoneweergave ook visueel nagekeken.
- HTML-tekstinhoud en ingebedde afbeeldingen vergeleken met de aangeleverde bestanden: ongewijzigd.
- git diff --check uitgevoerd.

## Ontbrekend en beperkingen

- Geen favicon aangeleverd. De browser vraagt automatisch /favicon.ico op en krijgt een 404. Geen vervanging toegevoegd.
- Telefoon- en e-maillinks zijn behouden. Er is niet gebeld en er is geen e-mail verstuurd.
- Tests zijn uitgevoerd in Chromium met aangepaste viewportgroottes, niet op fysieke toestellen of in Safari/Firefox.
- GitHub-toegang en schrijftoegang zijn in deze sessie bevestigd. Deze wijzigingen worden lokaal voorbereid; er is niet gepusht en niets gepubliceerd.

## Vervolg

Na review kan de voorbereide branch naar origin worden gepusht en eventueel als pull request worden aangeboden. Controleer vóór eventuele publicatie welke hostingworkflow de repository gebruikt. Openbare publicatie vereist eerst toestemming van de gebruiker.
