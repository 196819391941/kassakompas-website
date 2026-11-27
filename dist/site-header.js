const header = document.querySelector('header');
const primary = header?.querySelector('nav.links');
const languages = header?.querySelector('.language-switch');

if (header && primary && languages) {
  const language = document.documentElement.lang.split('-')[0];
  const labels = {
    nl: ['Kassasystemen & kassasoftware met persoonlijke service', 'Menu', 'Hoofdnavigatie', 'KassaKompas home', 'De juiste richting voor jouw zaak'],
    fr: ['Systèmes de caisse et logiciels avec un service personnalisé', 'Menu', 'Navigation principale', 'Accueil KassaKompas', 'La bonne direction pour votre activité'],
    en: ['POS systems and software with personal service', 'Menu', 'Main navigation', 'KassaKompas home', 'The right direction for your business'],
  };
  const [tagline, menu, navigation, homeLabel, motto] = labels[language] || labels.nl;
  const links = [...primary.querySelectorAll('a')];
  const [home, , , , , contact] = links;

  if (home && contact) {
    const bar = document.createElement('div');
    bar.className = 'site-header-note';
    bar.textContent = tagline;

    const row = document.createElement('div');
    row.className = 'site-header-row';

    const brand = document.createElement('a');
    brand.className = 'site-header-brand';
    brand.href = home.href;
    brand.setAttribute('aria-label', homeLabel);
    brand.innerHTML = '<span class="site-header-mark"><svg aria-hidden="true" width="25" height="25" viewBox="0 0 28 28" fill="none"><path d="M5 20.5 13.7 5l9.3 15.5h-7.4l-2-3.5-2 3.5H5Z" stroke="currentColor" stroke-width="1.7"></path><circle cx="14" cy="4.1" r="2.1" fill="#6c9cc0"></circle></svg></span><span>KassaKompas<small></small></span>';
    brand.querySelector('small').textContent = motto;

    const toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.className = 'site-header-toggle';
    const icon = document.createElement('span');
    icon.setAttribute('aria-hidden', 'true');
    icon.textContent = '☰';
    toggle.append(icon, ' ', menu);
    toggle.setAttribute('aria-controls', 'site-header-navigation');
    toggle.setAttribute('aria-expanded', 'false');

    primary.className = 'site-header-links';
    primary.id = 'site-header-navigation';
    primary.setAttribute('aria-label', navigation);
    for (const link of links) link.removeAttribute('class');
    contact.className = 'site-header-contact';
    const setOpen = open => toggle.setAttribute('aria-expanded', String(open));
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') === 'false'));
    primary.addEventListener('click', event => {
      if (event.target.closest('a')) setOpen(false);
    });
    header.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });

    header.className = 'site-header';
    row.append(brand, languages, toggle, primary);
    header.replaceChildren(bar, row);
  }
}
