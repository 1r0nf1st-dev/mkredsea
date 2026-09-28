"""Make a tightly-cropped copy of the client's logo badge.

The supplied badge sits in the middle of a mostly transparent canvas (the
artwork is only ~50% of the image's width), so wherever it's placed it shows
at about half the intended size. This trims the transparent border — same
artwork, not redesigned or recoloured — keeping a small margin, and writes an
800px web copy used by the alt sites.

Needs Pillow. Re-run from the project root:
    python3 scripts/crop-logo.py
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets/logo/mk-redsea-badge-original.png"
OUT = ROOT / "assets/logo/mk-redsea-badge-cropped.png"
SIZE = 800
MARGIN = 0.02  # of the artwork's size, on each side

img = Image.open(SRC).convert("RGBA")
left, top, right, bottom = img.getchannel("A").getbbox()
side = max(right - left, bottom - top)
pad = round(side * MARGIN)
cx, cy = (left + right) / 2, (top + bottom) / 2
half = side / 2 + pad
box = tuple(round(v) for v in (cx - half, cy - half, cx + half, cy + half))

cropped = img.crop(box).resize((SIZE, SIZE), Image.LANCZOS)
cropped.save(OUT, optimize=True)
print(f"wrote {OUT.relative_to(ROOT)} {cropped.size} from box {box}")
