## 2024-04-13 - Skip to Content Links

**Learning:** Skip-to-content links provide critical keyboard accessibility but were missing from the application's layout. Keyboard-only and screen reader users would have had to tab through the navigation menu on every single page load before reaching the main content.
**Action:** Adding a `<main id="main-content">` landmark wrapping the primary content and a visually-hidden (until focused) skip link at the very top of the `<body>` is a clean way to implement this pattern across all pages globally via the `BaseLayout`. Added global focus-visible indicators for better navigation visibility as well.

## 2024-04-15 - Dynamic Theme Tooltips and Semantic Lists

**Learning:**
1. Icon-only buttons (like the theme toggle) benefit greatly from dynamic `aria-label` and `title` attributes that reflect the *action* they will perform rather than a static description.
2. Generating list items (`<li>`) dynamically from components requires ensuring the component outputs the `<li>` tag directly if it's placed inside a `<ul>` or `<ol>`. Wrapping headings in anchor tags inside a list creates invalid HTML structure and a poor screen reader experience.
**Action:** Implemented dynamic state updates for the theme toggle's `aria-label` and `title`. Refactored `BlogPost.astro` to properly wrap the anchor in an `<li>` tag, improving semantic structure and accessibility.

## 2024-04-16 - Contextual Text and Interactive States for Links

**Learning:** Generic link text (e.g., just the platform name like "twitter") lacks action context for screen reader users. Additionally, abstract link components often miss proper focus and hover states which degrades keyboard navigation visibility.
**Action:** Added an `aria-label` to the `Social.astro` component to provide clear intent ("Follow on Twitter"), and added CSS transitions, hover, and focus-visible outlines to enhance interactive feedback.
