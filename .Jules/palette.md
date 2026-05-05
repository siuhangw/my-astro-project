## 2024-04-13 - Skip to Content Links

**Learning:** Skip-to-content links provide critical keyboard accessibility but were missing from the application's layout. Keyboard-only and screen reader users would have had to tab through the navigation menu on every single page load before reaching the main content.
**Action:** Adding a `<main id="main-content">` landmark wrapping the primary content and a visually-hidden (until focused) skip link at the very top of the `<body>` is a clean way to implement this pattern across all pages globally via the `BaseLayout`. Added global focus-visible indicators for better navigation visibility as well.

## 2024-04-15 - Dynamic Theme Tooltips and Semantic Lists

**Learning:**
1. Icon-only buttons (like the theme toggle) benefit greatly from dynamic `aria-label` and `title` attributes that reflect the *action* they will perform rather than a static description.
2. Generating list items (`<li>`) dynamically from components requires ensuring the component outputs the `<li>` tag directly if it's placed inside a `<ul>` or `<ol>`. Wrapping headings in anchor tags inside a list creates invalid HTML structure and a poor screen reader experience.
**Action:** Implemented dynamic state updates for the theme toggle's `aria-label` and `title`. Refactored `BlogPost.astro` to properly wrap the anchor in an `<li>` tag, improving semantic structure and accessibility.

## 2024-05-05 - External Links and Platform Casing

**Learning:** When linking to external social platforms, users expect them to open in a new tab so they don't lose their place on the blog. Additionally, raw platform names (e.g., 'twitter') look unpolished compared to capitalized names ('Twitter'). However, screen readers need explicit context about external link behavior to prevent confusion when a new tab opens unexpectedly.
**Action:** Always pair `target="_blank"` with `rel="noopener noreferrer"` for security, and add a dynamic `aria-label` (e.g., `Follow me on Twitter (opens in a new tab)`) to explicitly communicate the behavior to assistive technologies. Simple inline string manipulation (`{platform[0].toUpperCase() + platform.slice(1)}`) is an effective way to polish data-driven text without adding custom CSS classes.
