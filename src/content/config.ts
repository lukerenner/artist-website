import { defineCollection, z } from 'astro:content';

const booksCollection = defineCollection({
    type: 'data',
    schema: z.object({
        title: z.string(),
        slug: z.string(),
        coverImage: z.string(),
        blurb: z.string(),
        description: z.string(),
        buyUrl: z.string().optional(),
        order: z.number(),
        featured: z.boolean(),
        color: z.string().optional(),
    }),
});

const paintingsCollection = defineCollection({
    type: 'data',
    schema: z.object({
        title: z.string(),
        slug: z.string(),
        image: z.string(),
        medium: z.string(),
        dimensions: z.string().optional(),
        description: z.string(),
        order: z.number(),
    }),
});

const blogCollection = defineCollection({
    type: 'content',
    schema: z.object({
        title: z.string(),
        date: z.date(),
        description: z.string(),
        author: z.string().default('Bonnie Bostrom'),
    }),
});

export const collections = {
    books: booksCollection,
    paintings: paintingsCollection,
    blog: blogCollection,
};
