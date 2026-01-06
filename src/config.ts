export const siteConfig = {
    // Site metadata
    title: "Bonnie Bostrom | Painter, Poet, Author",
    description: "Official website of Bonnie Bostrom - Painter, Poet, and Author",

    // Domain configuration (use environment variable for staging vs production)
    url: process.env.SITE_URL || "https://bonniebostrom.com",

    // Ecommerce (Stripe Payment Links - outbound only, no cart/checkout)
    // TODO: Replace with actual Stripe Payment Links
    bornCrazyBuyUrl: "https://buy.stripe.com/test_placeholder",

    // Forms (Formspree - public endpoints with spam protection)
    // TODO: Replace with actual Formspree endpoints after account setup
    formspreeContactEndpoint: "https://formspree.io/f/placeholder",
    formspreeInquiryEndpoint: "https://formspree.io/f/placeholder",
};
