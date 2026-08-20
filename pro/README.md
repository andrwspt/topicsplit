# TopicSplit Pro

Batch semantic text grouper — split articles, transcripts, and notes into topic segments by meaning.

## Install

```bash
pip install topicsplit-pro
```

## Usage

### Split a single file

```bash
topicsplit split article.txt
# → article_topicsplit.md (clean markdown with ### Topic N headers)
```

### Batch split a folder of articles

```bash
topicsplit batch ./articles/
# → ./articles_topicsplit/ (one file per article, all split)
```

### Inline text (great for pipes)

```bash
echo "Long article text..." | topicsplit echo
```

### Adjust sensitivity

```bash
topicsplit split article.txt -s 0.3   # fewer, longer segments
topicsplit split article.txt -s 0.8   # more, shorter segments
```

## Features

- **Batch processing** — split entire folders in one command
- **Same algorithm** as the free web version (lexical cohesion / meaning-based)
- **Clean markdown output** — ready for Obsidian, Logseq, Notion
- **Sensitivity slider** — 0.0 (few segments) to 1.0 (many segments)
- **Preserves your text** — no rewriting, no AI, no server

## Pricing

TopicSplit Pro is **pay what you want** (minimum $5). Your support keeps the free web version alive and funds new tools.

**☕ [Pay via PayPal](https://paypal.me/andrwspt)** or **[Ko-fi](https://ko-fi.com/andrwspt)**

## Free version

The free, 100% offline web version is at <https://andrwspt.github.io/topicsplit/>.

## License

MIT
