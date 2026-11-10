# KassaKompas — exacte back-up van Sites-versie 31

Referentiewebsite: https://kassakompas-homepage-voorbeeld.bluishcity.chatgpt.site/#top

**De vastgelegde referentiewebsite staat in `source/dist/`.** De oudere bestanden buiten deze back-upmap zijn bewust behouden uit de bestaande GitHub-repository. Ze zijn niet als vervanging voor versie 31 gebruikt.

## Herkomst
- Sites-project: `appgprj_6af048855740819188b7a138cea7a2d8`
- Sites-versie: **31**
- Versie-ID: `appgprj_6af048855740819188b7a138cea7a2d8~appgver_ba2b44837994819190681e4c196c143e`
- Publicatie-ID: `appgdep_6af20cbe630081918ec1a0e00965119c`
- Brondatacommit: `d75bfa405c880535e6b3c0e2122a6ac2c45622b2`
- Exacte Git-tree van de bron: `02e4ef107c4d93fd3bdbef109a1c836db36eb5ee`
- Controle: 10 november 2026.

De Sites-API bevestigt versie 31 en de geslaagde publicatie op de referentie-URL. De Sites-bronrepository is opnieuw opgehaald en wijst naar bovenstaande commit. `source/` is rechtstreeks met `git archive` uit die commit gemaakt, niet uit een oude preview of uit gerenderde webpagina's.

## Inhoud
35 originele bronbestanden, waaronder:
- Homepage, Horeca, Retail en Koppelingen.
- Vijf gekoppelde horecasectoren: Restaurants, Fastfood, Koffiebars, Bars & clubs, Hotels.
- Alle 23 lokale assets, de inline/data-afbeeldingen en iconen in de HTML.
- De afzonderlijke proefpagina voor de snelheidszweem (niet toegepast op de homepage).
- `.openai/hosting.json` en `.gitignore`.

`SOURCE-SHA256SUMS` en `source-manifest.json` leggen de bestandsinhoud vast. Alle 34 bestanden van het lokaal bewaarde publicatiepakket zijn byte voor byte gelijk aan de corresponderende bestanden in `source/`. Het extra bronbestand `.gitignore` hoort niet bij het publicatiepakket.

## Belangrijke beperking: externe afhankelijkheden
**Deze back-up bevat de volledige originele broncode, maar is nog niet volledig zelfstandig/offline te herstellen.** Drie inhoudelijke afbeeldingen worden in de originele versie 31 vanaf externe websites geladen en zijn niet als lokale afbeeldingsbestanden aanwezig:

1. `horeca.html`: PAX A77-afbeelding
   https://shop.emerchantauthority.com/cdn/shop/products/A77_10_802615c1-9bdc-4ff4-8383-b6f2cce90d18.jpg?v=1637760261
2. `koppelingen.html`: Zoete Kruimels
   https://cdn-craftcms.dish.co/Nederland/Contentafbeeldingen/_squareBig/7464/Zoete-Kruimels-Instapkassa.webp
3. `koppelingen.html`: medewerker met tablet aan de bar
   https://cdn-craftcms.dish.co/Nederland/Contentafbeeldingen/_squareBig/8019/horeca-reserveringssysteem-tafels.webp

Het downloaden van deze bestanden is op 10 november 2026 in deze werkomgeving met HTTP 403 geblokkeerd. De oorspronkelijke verwijzingen zijn intact gebleven; er zijn geen vervangende of oudere afbeeldingen gebruikt. Bewaar de originele drie bestanden aanvullend om de website ook onafhankelijk van deze leveranciers te kunnen herstellen.

Er staan daarnaast al technische verwijzingen naar de Sites-werkbalk en browser/publicatiebestanden in de oorspronkelijke HTML. Deze zijn niet stilzwijgend gewijzigd. Een inventaris staat in `dependencies.json`. De native Sites-publicatie is via de Sites-API bevestigd; rechtstreeks HTTP uitlezen van de publieke referentie-URL werd eveneens geblokkeerd. Daarom is geen geslaagde onafhankelijke live-download of pixelvergelijking geclaimd.

## Lokaal bekijken
Vanuit `source/`:

```sh
python -m http.server 8080 --directory dist
```

Open daarna `http://localhost:8080/`. De originele interne routes en ankers blijven behouden. Externe afbeeldingen en de platformwerkbalk vereisen hun oorspronkelijke externe diensten.

Controleer de bestandschecksums vanuit deze back-upmap:

```sh
sha256sum -c SOURCE-SHA256SUMS
```

## Repositorybescherming
Deze snapshot is toegevoegd op een aparte branch vanaf GitHub-main-commit `3c7c94e3644ddc5b852e446773e85a56be9c1e73`. Er zijn geen bestaande bestanden verwijderd of overschreven en `main` is niet door deze back-up gewijzigd. Er is geen nieuwe website gepubliceerd of teruggezet.
