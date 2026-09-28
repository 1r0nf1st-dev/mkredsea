"""Colour-correct the client's own Red Sea photos and write the web copies
used by the main site (and, via alt*/scripts/grade-photos.py, the alts).

Reads the untouched originals in assets/photos/originals/ and writes:
  assets/photos/gallery/<name>.jpg      max 1600px wide, for large screens
  assets/photos/gallery/<name>-800.jpg  800px wide, for phones / srcset
  assets/photos/hero.jpg                the hero background (snapper-school)

The correction targets the usual underwater problems: a blue/cyan cast and
haze that flatten contrast and wash out the reds and yellows. Each channel is
levels-stretched between its own low/high percentiles (a per-channel
auto-levels, which neutralises the cast), blended back with the original by a
per-photo strength so the water stays blue rather than going grey, then given
a gentle contrast/saturation lift and an unsharp mask.

Needs Pillow + numpy. Re-run from the project root:
    python3 scripts/process-photos.py
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets/photos/originals"
OUT = ROOT / "assets/photos/gallery"

# name: (cast-correction strength 0..1, contrast, saturation)
PHOTOS = {
    "reef-wall":        (0.45, 1.08, 1.10),
    "bannerfish-pair":  (0.30, 1.12, 1.08),
    "split-lighthouse": (0.25, 1.05, 1.05),
    "snapper-school":   (0.40, 1.08, 1.08),
    "coral-pinnacle":   (0.65, 1.14, 1.12),
    "split-jetty":      (0.30, 1.06, 1.06),
    "sandy-reef":       (0.55, 1.10, 1.10),
}
HERO = "snapper-school"


def correct(img, strength, contrast, saturation):
    a = np.asarray(img, dtype=np.float32)
    stretched = np.empty_like(a)
    for c in range(3):
        lo, hi = np.percentile(a[..., c], (0.5, 99.5))
        stretched[..., c] = (a[..., c] - lo) * 255.0 / max(hi - lo, 1.0)
    out = a * (1 - strength) + np.clip(stretched, 0, 255) * strength
    img = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Color(img).enhance(saturation)
    return img.filter(ImageFilter.UnsharpMask(radius=1.6, percent=60, threshold=3))


def save(img, path, width):
    if img.width > width:
        img = img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)
    img.save(path, quality=84, optimize=True, progressive=True)
    print(f"wrote {path.relative_to(ROOT)} {img.size}")


OUT.mkdir(exist_ok=True)
for name, params in PHOTOS.items():
    img = correct(Image.open(SRC / f"{name}.jpg").convert("RGB"), *params)
    save(img, OUT / f"{name}.jpg", 1600)
    save(img, OUT / f"{name}-800.jpg", 800)
    if name == HERO:
        save(img, ROOT / "assets/photos/hero.jpg", 1600)
