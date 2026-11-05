#!/usr/bin/env python3
"""Record in a rendered PNG which source it was drawn from, so a stale copy can be caught without Chrome.

A PNG copy of an SVG or an HTML card can only be compared byte for byte by rendering it again, which needs Chrome and
the same fonts. Instead, when a generator renders a PNG it writes a `source-sha256` text chunk into it: the SHA-256 of
the source text plus every local file the source loads through `src="..."` (the screenshots on a family card). A
check then recomputes that digest from the committed source and fails when the PNG carries a different one, or none.
The chunk sits right after the PNG header and does not change a single pixel. Standard library only.
"""
import hashlib
import re
import struct
import zlib
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
KEY = b"source-sha256"
SRC = re.compile(r'\bsrc="([^"]+)"')


def source_digest(text, base):
    """SHA-256 over the source text and, in order, the bytes of each local file it loads with src="..."."""
    h = hashlib.sha256(text.encode("utf-8"))
    for ref in SRC.findall(text):
        if re.match(r"[a-z][a-z0-9+.-]*:", ref, re.I):
            continue  # a URL (data:, file:, https:), not a file beside the page
        path = (Path(base) / ref).resolve()
        h.update(b"\0" + ref.encode("utf-8") + b"\0")
        h.update(path.read_bytes() if path.is_file() else b"missing")
    return h.hexdigest()


def _chunks(data):
    if not data.startswith(PNG_MAGIC):
        raise ValueError("not a PNG")
    i = len(PNG_MAGIC)
    while i < len(data):
        length, kind = struct.unpack(">I4s", data[i:i + 8])
        yield kind, data[i + 8:i + 8 + length], data[i:i + 12 + length]
        i += 12 + length


def _text_chunk(key, value):
    body = key + b"\0" + value.encode("ascii")
    return struct.pack(">I", len(body)) + b"tEXt" + body + struct.pack(">I", zlib.crc32(b"tEXt" + body))


def read_stamp(path):
    """The source digest stamped into the PNG at path, or None if it has none or is not a PNG."""
    try:
        for kind, body, _ in _chunks(Path(path).read_bytes()):
            if kind == b"tEXt" and body.startswith(KEY + b"\0"):
                return body[len(KEY) + 1:].decode("ascii")
    except (OSError, ValueError, struct.error):
        return None
    return None


def stamp(path, digest):
    """Write the digest into the PNG at path, replacing any earlier stamp. Pixels are untouched."""
    path = Path(path)
    out = [PNG_MAGIC]
    for kind, body, raw in _chunks(path.read_bytes()):
        if kind == b"tEXt" and body.startswith(KEY + b"\0"):
            continue
        out.append(raw)
        if kind == b"IHDR":
            out.append(_text_chunk(KEY, digest))
    path.write_bytes(b"".join(out))


def stale(png, text, base):
    """None when the PNG at png carries the digest of this source, else a short reason."""
    png = Path(png)
    if not png.is_file():
        return "missing"
    found = read_stamp(png)
    if found is None:
        return "has no source stamp"
    if found != source_digest(text, base):
        return "was rendered from a different source"
    return None
