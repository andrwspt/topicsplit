"""Core semantic splitting algorithm — matches web version behavior."""

import re
from typing import List, Tuple

STOP_WORDS = set(
    "a an the and or but if then of to in on at by for with as is are was were "
    "be been being this that these those it its he she they we you i me my your "
    "our their from into about over under between which who what when where why "
    "how not no do does did have has had will would can could should may might "
    "must also than so such only own same each more most other some any all both "
    "few many one two three first second".split()
)


def sentences(text: str) -> List[str]:
    """Split text into sentences."""
    return [
        s.strip()
        for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text).strip())
        if s.strip()
    ]


def words(s: str) -> List[str]:
    """Extract content words (non-stopwords, length > 3)."""
    return [
        w
        for w in re.sub(r"[^a-z0-9\s]", " ", s.lower()).split()
        if len(w) > 3 and w not in STOP_WORDS
    ]


def overlap(a: List[str], b: List[str]) -> float:
    """Cosine-like overlap between two word lists."""
    if not a or not b:
        return 0.0
    sa, sb = set(a), set(b)
    inter = len(sa & sb)
    return inter / ((len(sa) * len(sb)) ** 0.5 or 1)


def split_text(
    text: str,
    sensitivity: float = 0.55,
    skip_tiny: bool = True,
    min_segment_words: int = 6,
) -> List[Tuple[str, int]]:
    """
    Split text into topic segments by lexical cohesion.

    sensitivity: 0.0 = few segments, 1.0 = many segments.
    Returns list of (segment_text, sentence_count) tuples.
    """
    sents = sentences(text)
    if len(sents) < 2:
        return [(text, len(sents))]

    ws = [words(s) for s in sents]
    coh = [overlap(ws[i], ws[i + 1]) for i in range(len(sents) - 1)]

    if not coh:
        return [(text, len(sents))]

    mean_val = sum(coh) / len(coh)
    sd_val = (sum((c - mean_val) ** 2 for c in coh) / len(coh)) ** 0.5

    # Inverse: higher sensitivity = lower threshold = more cuts = more segments
    thr = max(0.0, mean_val - (1.0 - sensitivity) * (mean_val + sd_val))

    segs = []
    cur = [sents[0]]
    for i, c in enumerate(coh):
        if c < thr:
            segs.append(" ".join(cur))
            cur = [sents[i + 1]]
        else:
            cur.append(sents[i + 1])
    segs.append(" ".join(cur))

    if skip_tiny:
        merged = []
        for g in segs:
            tok = g.split()
            if tok and len(tok) < min_segment_words and merged:
                merged[-1] += " " + g
            else:
                merged.append(g)
        segs = merged

    # Return with sentence counts
    result = []
    for idx, seg in enumerate(segs):
        n = len(sentences(seg))
        result.append((f"### Topic {idx + 1}\n{seg}", n))
    return result


def render_markdown(segments: List[Tuple[str, int]]) -> str:
    """Render segments as clean markdown."""
    return "\n\n".join(seg for seg, _ in segments)
