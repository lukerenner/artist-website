import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Use environment variable for site URL, defaulting to production
const site = process.env.SITE_URL || 'https://bonniebostrom.com';

// https://astro.build/config
export default defineConfig({
    site: site,
    base: '/',
    output: 'static',
    build: {
        assets: 'assets'
    },
    integrations: [sitemap()]
});
