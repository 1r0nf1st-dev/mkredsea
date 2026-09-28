"""Apply a moody blue-gray duotone grade to the site photos, to match the
alt design's visual language. Converts each photo to grayscale by
luminance, then recolors shadows-to-highlights along a dark navy -> pale
blue-gray ramp (ImageOps.colorize), with a slight contrast boost.

- assets/photos/<name>-raw.jpg -> assets/photos/<name>.jpg (hero, about, courses)
- the main site's colour-corrected gallery (../assets/photos/gallery/, made by
  scripts/process-photos.py) -> assets/photos/gallery/ here

Paths are relative to this script, so the same file works in alt/, alt2/ and
alt3/. Source credits: see assets/photos/SOURCES.md
"""
from pathlib import Path

from PIL import Image, ImageOps, ImageEnhance

SITE_DIR = Path(__file__).resolve().parent.parent
PHOTO_DIR = SITE_DIR / "assets/photos"
GALLERY_SRC = SITE_DIR.parent / "assets/photos/gallery"
GALLERY_OUT = PHOTO_DIR / "gallery"

FILES = ["hero", "about", "course-discovery", "course-specialty", "course-divemaster"]

SHADOW = (8, 16, 24)      # near-black navy
MID = (46, 74, 92)        # slate blue
HIGHLIGHT = (214, 226, 230)  # pale blue-gray


def grade(src, out_path):
    img = Image.open(src).convert("RGB")
    img = ImageEnhance.Contrast(img).enhance(1.12)
    gray = ImageOps.grayscale(img)
    gray = ImageOps.autocontrast(gray, cutoff=1)
    duotone = ImageOps.colorize(gray, black=SHADOW, mid=MID, white=HIGHLIGHT, midpoint=127)
    duotone = ImageEnhance.Color(duotone).enhance(1.05)
    duotone.save(out_path, quality=87, progressive=True)
    print(f"wrote {out_path.relative_to(SITE_DIR.parent)} {duotone.size}")


for name in FILES:
    grade(PHOTO_DIR / f"{name}-raw.jpg", PHOTO_DIR / f"{name}.jpg")

GALLERY_OUT.mkdir(exist_ok=True)
for src in sorted(GALLERY_SRC.glob("*.jpg")):
    grade(src, GALLERY_OUT / src.name)
