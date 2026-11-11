# Contactaanvragen activeren

Status: sales@kassakompas.com is volgens de gebruiker nog niet actief. De website biedt daarom telefonisch contact; het online formulier is zichtbaar maar uitgeschakeld. Alle contact- en adviesknoppen leiden naar /contact/; onderwerpcontext gaat mee via de querystring. Telefoonlinks blijven direct werken.

Voor activering:
1. Activeer en test sales@kassakompas.com, inclusief ontvangst van externe e-mail.
2. Kies en configureer een echte formulierverzenddienst of serverendpoint met dit adres als ontvanger. Een actieve mailbox alleen levert geen formulierendpoint.
3. Voeg servervalidatie, spambeperking en correcte fout- en succesmeldingen toe. Behoud de ingevulde aanvraag bij een fout.
4. Leg de informatie over verwerking van persoonsgegevens vast op basis van de werkelijke dienst en bewaartermijnen.
5. Test een echte inzending tot en met ontvangst in de mailbox. Schakel daarna de velden en verzendknop in en werk de tijdelijke meldingen bij.
6. Publiceer met behoud van zichtbaarheid en maak direct de volledige, geverifieerde GitHub-back-up op een aparte branch.
