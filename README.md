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
2. Paste text.
3. Drag **Sensitivity** (higher = more, smaller segments).
4. Click **Split into topics** → get clean `### Topic N` markdown.
5. **Copy markdown** or **Download .md** straight into Obsidian / Logseq.

## License
MIT — do whatever you want with it.

---

## Support the work
This is free. If it saves you time, the easiest way to say thanks is **$1**:

- **Ko-fi** → https://ko-fi.com/andrwspt (one-time or monthly, any amount from $1)
- **PayPal.me** → https://paypal.me/andrwspt (one-time tip)
- (GitHub Sponsors available too once enabled on the repo)

Every dollar goes back into building more free, private, offline tools.
