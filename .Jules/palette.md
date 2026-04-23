## 2024-04-13 - Skip to Content Links

**Learning:** Skip-to-content links provide critical keyboard accessibility but were missing from the application's layout. Keyboard-only and screen reader users would have had to tab through the navigation menu on every single page load before reaching the main content.
**Action:** Adding a `<main id="main-content">` landmark wrapping the primary content and a visually-hidden (until focused) skip link at the very top of the `<body>` is a clean way to implement this pattern across all pages globally via the `BaseLayout`. Added global focus-visible indicators for better navigation visibility as well.

## 2024-04-15 - Dynamic Theme Tooltips and Semantic Lists

**Learning:**
1. Icon-only buttons (like the theme toggle) benefit greatly from dynamic `aria-label` and `title` attributes that reflect the *action* they will perform rather than a static description.
2. Generating list items (`<li>`) dynamically from components requires ensuring the component outputs the `<li>` tag directly if it's placed inside a `<ul>` or `<ol>`. Wrapping headings in anchor tags inside a list creates invalid HTML structure and a poor screen reader experience.
**Action:** Implemented dynamic state updates for the theme toggle's `aria-label` and `title`. Refactored `BlogPost.astro` to properly wrap the anchor in an `<li>` tag, improving semantic structure and accessibility.

## 2024-04-23 - External Links and Context
**Learning:** Opening links in a new tab without warning screen reader users can be confusing and disorienting. Also, visual flair (like capitalizing link text) can help standard lowercase data ("github") look polished while screen readers get the descriptive `aria-label`.
**Action:** Always pair `target="_blank"` with an `aria-label` specifying "(opens in a new tab)" to provide proper context. Use CSS `text-transform: capitalize` for consistent text styling of lowercase platform data, and combine with smooth hover/focus transitions (`translateY`) for interactive visual feedback.
