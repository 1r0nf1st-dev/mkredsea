#!/usr/bin/env python3
"""One-off extraction of the client's original logo/favicon PNGs.

These were embedded as base64 data URIs in mkredsea-holding2.html (the old
"coming soon" holding page). This script decodes them back out to real files
so the real site can reference them normally instead of inlining them.

This does NOT redesign or recolor anything — it just decodes bytes that
were already there. Run again any time the extracted files need to be
regenerated from the holding page.
"""
import base64
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "mkredsea-holding2.html"

TARGETS = [
    (r'sizes="32x32" href="data:image/png;base64,([A-Za-z0-9+/=]+)"',
     ROOT / "assets" / "favicon" / "favicon-32.png"),
    (r'apple-touch-icon" href="data:image/png;base64,([A-Za-z0-9+/=]+)"',
     ROOT / "assets" / "favicon" / "apple-touch-icon.png"),
    (r'class="logo" src="data:image/png;base64,([A-Za-z0-9+/=]+)"',
     ROOT / "assets" / "logo" / "mk-redsea-badge-original.png"),
]


def main():
    html = SOURCE.read_text()
    for pattern, out_path in TARGETS:
        match = re.search(pattern, html)
        if not match:
            raise SystemExit(f"Could not find pattern in {SOURCE}: {pattern}")
        data = base64.b64decode(match.group(1))
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(data)
        print(f"Wrote {out_path} ({len(data):,} bytes)")


if __name__ == "__main__":
    main()
