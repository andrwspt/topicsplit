# TopicSplit

A tiny, **offline** tool that groups pasted text into topic segments by lexical
cohesion — no server, no API key, no tracking. Open `index.html` in any browser
**👉 Live demo:** https://andrwspt.github.io/topicsplit/

and it just works.

It was built from a simple principle: **split where meaning shifts, not where a
fixed word count runs out.** Consecutive sentences that share few content words
are probably changing subject; that's where the cut goes. A sensitivity slider
tunes how aggressively it splits.

## Why it exists
Note-takers, writers, and researchers constantly face a wall of text they need to
break into atoms. Most "summarizers" need an account and ship your text to a
server. TopicSplit runs entirely on your machine.

## How to use
1. Open `index.html` (double-click — no install).
2. Paste text — or click **"Try with sample text"** for an instant demo.
3. Drag **Sensitivity** (higher = more, smaller segments).
4. Click **Split into topics** → get clean `### Topic N` markdown.
5. **Copy markdown** or **Download .md** straight into Obsidian / Logseq.

## What's new in v1.2
- **"Try with sample text" button** — no need to find/paste text to demo it
- **Post-split tip bar** — a gentle ask at the exact moment you see value

## License
MIT — do whatever you want with it.

---

## Support the work

This tool is free and will stay free. If it saved you time (or just blew your mind a tiny bit), the easiest way to say thanks is **$1** — that's it:

- **☕ Ko-fi → https://ko-fi.com/andrwspt** (one-time or monthly, any amount)
- **💳 PayPal.me → https://paypal.me/andrwspt** (one-time tip)

Every dollar goes back into building more free, private, offline tools.
No accounts. No tracking. Just text in, topics out.
