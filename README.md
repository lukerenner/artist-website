# Bonnie Bostrom Website

Static website for Bonnie Bostrom - Painter, Poet, and Author. Built with Astro and deployed to GitHub Pages.

## 🚀 Quick Start

### Local Development

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

The site will be available at `http://localhost:4321`

### Deployment

#### Staging (bonnie.lukerenner.co)
```bash
SITE_URL=https://bonnie.lukerenner.co npm run build
```

#### Production (bonniebostrom.com)
```bash
SITE_URL=https://bonniebostrom.com npm run build
```

Or simply:
```bash
npm run build  # Defaults to bonniebostrom.com
```

## 📝 Content Management

### Adding/Editing Books

Books are stored in `src/content/books/` as JSON files. Each book follows this schema:

```json
{
  "title": "Book Title",
  "slug": "book-title",
  "coverImage": "/images/books/book-title.webp",
  "blurb": "Short one-liner description",
  "description": "Full description with multiple paragraphs...",
  "buyUrl": "https://buy.stripe.com/...",  // Optional
  "order": 1,
  "featured": false
}
```

To add a new book:
1. Add the book cover image to `public/images/books/`
2. Create a new JSON file in `src/content/books/` (e.g., `new-book.json`)
3. Fill in the book details following the schema above
4. The book will automatically appear on the site

### Adding/Editing Paintings

Paintings are stored in `src/content/paintings/` as JSON files. Each painting follows this schema:

```json
{
  "title": "Painting Title",
  "slug": "painting-title",
  "image": "/images/paintings/painting-title.webp",
  "medium": "Acrylic on canvas",
  "size": "24x36 inches",
  "price": "$500",
  "description": "Description of the painting...",
  "available": true,
  "order": 1
}
```

To add a new painting:
1. Add the painting image to `public/images/paintings/`
2. Create a new JSON file in `src/content/paintings/` (e.g., `new-painting.json`)
3. Fill in the painting details following the schema above
4. The painting will automatically appear in the catalog and inquiry form dropdown

### Adding Blog Posts

Blog posts are stored in `src/content/blog/` as Markdown files with frontmatter:

```markdown
---
title: "Post Title"
date: 2026-01-05
description: "Brief description of the post"
author: "Bonnie Bostrom"
---

Your blog post content here in Markdown format...
```

## ⚙️ Configuration

### Site Configuration

Edit `src/config.ts` to update:

- **Stripe Payment Links**: Update `bornCrazyBuyUrl` with your Stripe Payment Link
- **Formspree Endpoints**: Update form endpoints after creating your Formspree account

```typescript
export const siteConfig = {
  // ... other config
  
  // Ecommerce
  bornCrazyBuyUrl: "https://buy.stripe.com/YOUR_LINK_HERE",
  
  // Forms
  formspreeContactEndpoint: "https://formspree.io/f/YOUR_ENDPOINT",
  formspreeInquiryEndpoint: "https://formspree.io/f/YOUR_ENDPOINT",
};
```

### Formspree Setup

1. Create a free account at [formspree.io](https://formspree.io)
2. Create two forms:
   - Contact Form
   - Painting Inquiry Form
3. Copy the form endpoints and update `src/config.ts`
4. Forms include honeypot spam protection automatically

### Stripe Payment Links

1. Create a Stripe account at [stripe.com](https://stripe.com)
2. Create Payment Links for your books:
   - Go to Stripe Dashboard → Payment Links
   - Create a new Payment Link for each book
   - Copy the link URL
3. Update the `buyUrl` field in the book's JSON file

## 🖼️ Image Management

### Image Optimization

All images should be converted to WebP format for optimal performance:

```bash
# Using ImageMagick or similar tool
convert input.jpg -quality 85 output.webp
```

### Responsive Images

For hero and painting images, create two sizes:
- `@1x` - Standard resolution
- `@2x` - High resolution for retina displays

Example:
- `hero-image.webp` (1920px wide)
- `hero-image@2x.webp` (3840px wide)

### Image Locations

- **Book covers**: `public/images/books/`
- **Paintings**: `public/images/paintings/`
- **Hero images**: `public/images/hero/`
- **About page**: `public/images/about/`

## 🌐 Deployment to GitHub Pages

### Initial Setup

1. Create a GitHub repository
2. Push your code to the repository
3. Enable GitHub Pages in repository settings:
   - Go to Settings → Pages
   - Source: GitHub Actions

### GitHub Actions Workflow

The site uses GitHub Actions for automatic deployment. The workflow file is located at `.github/workflows/deploy.yml`.

Every push to the `main` branch will automatically build and deploy the site.

### Custom Domain Setup

#### For Staging (bonnie.lukerenner.co)

1. Add a `CNAME` file to `public/` with content: `bonnie.lukerenner.co`
2. Configure DNS to point to GitHub Pages
3. Enable HTTPS in GitHub Pages settings

#### For Production (bonniebostrom.com)

1. Add a `CNAME` file to `public/` with content: `bonniebostrom.com`
2. Configure DNS:
   - Add an `A` record pointing to GitHub Pages IPs
   - Or add a `CNAME` record pointing to `<username>.github.io`
3. Enable HTTPS in GitHub Pages settings

## 📦 Project Structure

```
bonniebostrom-site/
├── .github/workflows/    # GitHub Actions deployment
├── public/              # Static assets
│   ├── images/         # All images
│   ├── favicon.png
│   └── robots.txt
├── src/
│   ├── components/     # Reusable components
│   ├── content/        # Content collections
│   │   ├── books/     # Book JSON files
│   │   ├── paintings/ # Painting JSON files
│   │   └── blog/      # Blog markdown files
│   ├── layouts/       # Page layouts
│   ├── pages/         # Site pages
│   ├── styles/        # Global styles
│   └── config.ts      # Site configuration
├── astro.config.mjs   # Astro configuration
└── package.json
```

## 🔧 Troubleshooting

### Build Fails

- Check that all image paths in content files are correct
- Ensure all required fields in book/painting schemas are filled
- Verify Formspree endpoints are valid URLs

### Forms Not Working

- Verify Formspree endpoints in `src/config.ts`
- Check that honeypot field is not being filled by real users
- Review Formspree dashboard for submission logs

### Images Not Loading

- Ensure images are in the correct `public/images/` subdirectory
- Check that image paths in content files start with `/images/`
- Verify image files are committed to the repository

## 📄 License

Copyright © 2026 Bonnie Bostrom. All rights reserved.
