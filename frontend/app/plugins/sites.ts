// plugins/sites.js
export default defineNuxtPlugin(() => {
    interface Site {
        name: string;
        domain: string;
        logo: string;
    }

    const sites: Site[] = [
        { name: 'Welcome To The jungle', domain: 'welcometothejungle.com', logo: 'welcomeToTheJungle.svg' },
        { name: 'LinkedIn', domain: 'linkedin.com', logo: 'linkedIn.svg' },
        { name: 'Hello Work', domain: 'hellowork.com', logo: 'helloWork.svg' },
        { name: 'France Travail', domain: 'francetravail.fr', logo: 'franceTravail.svg' },
    ];

  return {
    provide: {
      sites,
    },
  };
});