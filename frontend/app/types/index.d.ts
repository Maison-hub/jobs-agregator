export { sites };

declare global {
    interface sites {
        name: string;
        domain: string;
        logo: string;
    }
}