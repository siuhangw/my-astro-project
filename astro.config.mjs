import { defineConfig } from "astro/config";
import content from '@astrojs/content';
import cloudflare from "@astrojs/cloudflare";

import preact from "@astrojs/preact";

// https://astro.build/config
export default defineConfig({
  adapter: cloudflare(),
  site: "https://example.com",
  integrations: [content()],
  integrations: [preact()]
});