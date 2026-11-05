# Visuele controle — 5 november 2026

De openbare website en main zijn niet gewijzigd. Deze schermafbeeldingen tonen de voorgestelde versie. Download de drie HTML-bestanden van deze branch samen in één map en open index.html om de versie lokaal te bekijken; alle afbeeldingen zijn ingebed.

| Pagina | Desktop | Tablet | Smartphone | Kleine smartphone |
| --- | --- | --- | --- | --- |
| Home | [1440 px](index-1440.jpg) | [768 px](index-768.jpg) | [390 px](index-390.jpg) | [320 px](index-320.jpg) |
| Horeca | [1440 px](horeca-1440.jpg) | [768 px](horeca-768.jpg) | [390 px](horeca-390.jpg) | [320 px](horeca-320.jpg) |
| Retail | [1440 px](retail-1440.jpg) | [768 px](retail-768.jpg) | [390 px](retail-390.jpg) | [320 px](retail-320.jpg) |

## Wijzigingen

- Homepage: bevestigde retail- en horecaprijs met btw-vermelding en koopmogelijkheid; derde kaart behouden.
- Retail en Horeca: prijs direct onder de hoofdtitel; bestaande verdere inhoud behouden. Oude prijs ook vervangen in retail-FAQ en prijssecties.
- Paginatitels, metabeschrijvingen en sociale metadata aangepast; retail WebPage-schema consistent gemaakt.
- Kioskkaart (Afhaal & zelfbediening) en andere horecakaarten op smartphone in één kolom. Veilige gridbreedtes en tekstomloop; retailsectoren onder 421 px in één kolom.
- Geen Prijzen-pagina of links daarnaartoe toegevoegd. Geen aankoopbedragen of inclusies verzonnen.

## Controle

Chromium op 1440×900, 768×1024, 390×844 en 320×720 voor alle drie pagina’s: geen horizontale documentoverloop of interne kaartoverloop; alle afbeeldingen en CSS-achtergronden gedecodeerd; alle navigatielinks zichtbaar; alle lokale ankerdoelen aanwezig; geen JavaScript-fouten. Homepagekaarten naar Retail en Horeca met muis, Enter en spatie getest op alle vier breedtes (24 interacties).

Alle ingebedde afbeeldingen zijn byte voor byte gelijk aan de oorspronkelijke versie. Oude instapprijs afwezig in de HTML, inclusief metadata en schema. Telefoonnummer met eindcijfers 58 blijft terecht behouden. git diff --check geslaagd.

Tests gebruiken aangepaste Chromium-viewports, geen fysieke apparaten of Safari/Firefox. Telefoon- en e-maillinks behouden, zonder te bellen of mailen.

Terugvalversie: branch backup/voor-prijsaanpassing-2026-11-05, oorspronkelijke commit af76edc3f75861717160cf80459eedf4e43bd317.

Samenvoegen en publiceren pas na visuele goedkeuring.
