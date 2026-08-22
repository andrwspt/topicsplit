# Changelog

All notable changes to this project will be documented in this file.

## [1.8.1] — 2026-08-22

### Added
- **Auto-demo on shared links** — `?demo=1` URL param auto-loads sample text + splits instantly, so shared links show the tool working (no blank page)
- **Beautiful shareable result card** — "Share card" button generates a stats card (segments/sentences/words) with topic preview and one-click tweet/copy
- **Launch execution page** — `launch.html` with pre-filled copy for every community (Reddit, HN, Twitter, LinkedIn, Discord) and one-click submit buttons + pre-post checklist
- **Stronger conversion copy** — value-moment CTA says "This split took 0.003s. If it saved you 5 minutes of manual work, a $1 tip..." (concrete, timely, gratitude-based)

### Improved
- **Distribution page** — header "LAUNCH →" button links to launch.html for immediate execution
- **Challenge bar** — now specifies "Obsidian, Logseq, or Notion" to trigger recognition
- **Share buttons** — all shared links use `?demo=1` so new visitors see instant demo
- **Payout wiring** — `.github/FUNDING.yml` confirmed present (`ko_fi: andrwspt` + `custom: paypal.me/andrwspt`)

## [1.8.0] — 2026-08-22

### Added
- **SEO guide page** — `split-text-by-meaning.html` targets high-intent search queries
- **Tools hub page** — `tools.html` cross-lists all Andrew tools
- **Updated sitemap.xml** — includes all pages for Google indexing
- **Updated robots.txt** — points to sitemap

## [1.7.0] — 2026-08-21

### Added
- **Attribution in every export** — every copy/download includes `Split with [TopicSplit](link)` backlink
- **Share buttons** — after splitting, users get one-click Tweet/LinkedIn/Reddit/Email share buttons
- **Embed widget** — copy-paste iframe code to embed TopicSplit on any site
- **Badge widget** — copy-paste "Powered by TopicSplit" badge for blogs/docs
- **"Challenge a friend" prompt** — post-split nudge to share with note-taking friends

## [1.5.0] — 2026-08-21

### Added
- **JSON-LD structured data** — SoftwareApplication + FAQPage schema
- **Auto-load sample text** — first visitors see the tool working instantly
- **Testimonial section** — social proof above the fold

## [1.4.0] — 2026-08-20

### Added
- **Sticky CTA bar** — always-visible bottom bar with Ko-fi and PayPal buttons
- **Social proof badges** — live stats (GitHub stars, demo views, zero bytes sent)
- **Pro section** — promotes the CLI batch processor for power users
- **Animated tip bar** — appears after a successful split with direct Ko-fi link

## [1.2.0] — 2026-08-20

### Added
- **"Try with sample text" button** — one-click demo without pasting anything
- **Post-split tip bar** — appears after a successful split with direct Ko-fi link

## [1.0.0] — 2026-08-16

### Added
- First public release: paste text, set sensitivity, split into topic segments
- Download .md and Copy markdown buttons
- MIT License
- Ko-fi and PayPal tip buttons in footer
- .github/FUNDING.yml for GitHub Sponsors integration
