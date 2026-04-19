## 2024-04-13 - Skip to Content Links

**Learning:** Skip-to-content links provide critical keyboard accessibility but were missing from the application's layout. Keyboard-only and screen reader users would have had to tab through the navigation menu on every single page load before reaching the main content.
**Action:** Adding a `<main id="main-content">` landmark wrapping the primary content and a visually-hidden (until focused) skip link at the very top of the `<body>` is a clean way to implement this pattern across all pages globally via the `BaseLayout`. Added global focus-visible indicators for better navigation visibility as well.

## 2024-04-15 - Dynamic Theme Tooltips and Semantic Lists

**Learning:**
1. Icon-only buttons (like the theme toggle) benefit greatly from dynamic `aria-label` and `title` attributes that reflect the *action* they will perform rather than a static description.
2. Generating list items (`<li>`) dynamically from components requires ensuring the component outputs the `<li>` tag directly if it's placed inside a `<ul>` or `<ol>`. Wrapping headings in anchor tags inside a list creates invalid HTML structure and a poor screen reader experience.
**Action:** Implemented dynamic state updates for the theme toggle's `aria-label` and `title`. Refactored `BlogPost.astro` to properly wrap the anchor in an `<li>` tag, improving semantic structure and accessibility.

## 2024-05-20 - External Links Context and Interaction

**Learning:** When external social links are presented, opening them in a new tab without providing context causes accessibility issues for screen readers. Furthermore, lacking a visual indication (e.g., hover states) makes the UI feel static and unresponsive. Adding an `aria-label` that announces "(opens in a new tab)" provides essential context for non-sighted users, while hover animations and capitalized platform names greatly improve visual feedback and polish for sighted users.
**Action:** Updated social link components to include `target="_blank"`, `rel="noopener noreferrer"`, an `aria-label` stating it opens in a new tab, `text-transform: capitalize`, and a gentle transition effect on hover/focus to improve overall responsiveness and accessibility.
