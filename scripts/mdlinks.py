"""Shared markdown link helpers (standard library only)."""
import re
from pathlib import Path

_FENCE = re.compile(r"^\s*(```|~~~)")
_INLINE_CODE = re.compile(r"`[^`\n]*`")
_LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
_EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)", re.I)


def relative_links(text):
    """Yield (line_number, target) for each relative link or image, skipping code."""
    in_fence = False
    for n, line in enumerate(text.splitlines(), 1):
        if _FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for m in _LINK.finditer(_INLINE_CODE.sub("", line)):
            target = m.group(1)
            if target.startswith("#") or _EXTERNAL.match(target):
                continue
            yield n, target


def resolve(source, target):
    """Resolve a link target (fragment and query dropped) against the linking file."""
    path = re.split(r"[#?]", target, maxsplit=1)[0]
    return (Path(source).parent / path).resolve() if path else Path(source).resolve()


def broken_links(source):
    """Return [(line, target)] for relative links in `source` that do not resolve to a file or dir."""
    text = Path(source).read_text(encoding="utf-8")
    return [(n, t) for n, t in relative_links(text) if not resolve(source, t).exists()]
