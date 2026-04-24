## 2024-04-13 - Skip to Content Links

**Learning:** Skip-to-content links provide critical keyboard accessibility but were missing from the application's layout. Keyboard-only and screen reader users would have had to tab through the navigation menu on every single page load before reaching the main content.
**Action:** Adding a `<main id="main-content">` landmark wrapping the primary content and a visually-hidden (until focused) skip link at the very top of the `<body>` is a clean way to implement this pattern across all pages globally via the `BaseLayout`. Added global focus-visible indicators for better navigation visibility as well.

## 2024-04-15 - Dynamic Theme Tooltips and Semantic Lists

**Learning:**
1. Icon-only buttons (like the theme toggle) benefit greatly from dynamic `aria-label` and `title` attributes that reflect the *action* they will perform rather than a static description.
2. Generating list items (`<li>`) dynamically from components requires ensuring the component outputs the `<li>` tag directly if it's placed inside a `<ul>` or `<ol>`. Wrapping headings in anchor tags inside a list creates invalid HTML structure and a poor screen reader experience.
**Action:** Implemented dynamic state updates for the theme toggle's `aria-label` and `title`. Refactored `BlogPost.astro` to properly wrap the anchor in an `<li>` tag, improving semantic structure and accessibility.

## 2026-04-24 - Interactive States and External Links Context
**Learning:** External links opening in a new tab without an explicit warning are disruptive for screen reader users and those navigating with a keyboard. Furthermore, flat UI components lacking `:hover`, `:focus`, and `:active` styling degrade the tactile experience, causing a lack of interactivity feedback.
**Action:** When using external links, always apply `target="_blank"`, secure them with `rel="noopener noreferrer"`, and include an `aria-label` stating "(opens in a new tab)". Always include subtle `:hover`, `:focus`, and `:active` transitions (like slight scaling) to provide clear user feedback on interactions.
