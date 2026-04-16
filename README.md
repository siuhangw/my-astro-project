# My Astro Project

This is a personal blog and website built using [Astro](https://astro.build/). It is optimized for speed, utilizes Preact for interactive UI components, and is configured for deployment on Cloudflare Pages/Workers.

## Technologies Used

*   **Astro:** A modern web framework optimized for speed and content-heavy websites.
*   **Preact:** A lightweight alternative to React used for interactive components.
*   **Cloudflare Pages/Workers:** Edge deployment and hosting environment.
*   **Content Collections:** For managing and organizing blog posts (Markdown).

## Project Structure

*   `src/pages/`: Contains the main pages of the site (e.g., Home, About, Blog, Contact). It also handles dynamic routing for individual blog posts and tags.
*   `src/components/`: Reusable UI elements like Header, Footer, Navigation, and Preact components.
*   `src/layouts/`: Base layouts and Markdown-specific layouts.
*   `src/blog/`: Markdown files representing blog posts.

## Getting Started

### Prerequisites

*   Node.js (LTS version recommended)
*   npm

### Installation

1.  Clone the repository.
2.  Install dependencies:

    ```bash
    npm install
    ```

### Running Locally

To start the local development server:

```bash
npm run dev
```

The server will typically start at `http://localhost:4321/`.

### Building for Production

To build the project for production (generates the `dist/` directory):

```bash
npm run build
```

*Note: Depending on your environment, you may need to ensure execution permissions for the Astro binary before building (`chmod +x ./node_modules/.bin/astro`).*

## Deployment

This project uses `@astrojs/cloudflare` and `wrangler` to deploy to Cloudflare.

You can preview the production build locally:

```bash
npm run preview
```
