"""Apply a moody blue-gray duotone grade to the licensed stock photos, to
match the alt design's visual language. Converts each *-raw.jpg to
grayscale by luminance, then recolors shadows-to-highlights along a dark
navy -> pale blue-gray ramp (ImageOps.colorize), with a slight contrast
boost. Source credits: see alt/assets/photos/SOURCES.md
"""
from PIL import Image, ImageOps, ImageEnhance

SRC_DIR = "/Users/1r0nf1st/mkredsea/alt/assets/photos/"

FILES = ["hero", "about", "course-discovery", "course-specialty", "course-divemaster"]

SHADOW = (8, 16, 24)      # near-black navy
MID = (46, 74, 92)        # slate blue
HIGHLIGHT = (214, 226, 230)  # pale blue-gray

for name in FILES:
    img = Image.open(SRC_DIR + name + "-raw.jpg").convert("RGB")
    img = ImageEnhance.Contrast(img).enhance(1.12)
    gray = ImageOps.grayscale(img)
    gray = ImageOps.autocontrast(gray, cutoff=1)
    duotone = ImageOps.colorize(gray, black=SHADOW, mid=MID, white=HIGHLIGHT, midpoint=127)
    duotone = ImageEnhance.Color(duotone).enhance(1.05)
    out_path = SRC_DIR + name + ".jpg"
    duotone.save(out_path, quality=87)
    print(f"wrote {out_path} {duotone.size}")
