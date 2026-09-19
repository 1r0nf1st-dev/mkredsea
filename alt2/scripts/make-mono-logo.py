"""Generate solid-white and solid-black silhouette versions of the client's
logo badge for use against the alt design's dark nav overlay / light sections.

Keeps the exact alpha mask from the original artwork (same silhouette —
turtle, fish, coral, waves, text) and just recolors every opaque pixel.
Not a redesign, a straight recolor of the existing shape.
"""
import numpy as np
from PIL import Image

SRC = "/Users/1r0nf1st/mkredsea/assets/logo/mk-redsea-badge-original.png"
OUT_DIR = "/Users/1r0nf1st/mkredsea/alt/assets/logo/"

src = Image.open(SRC).convert("RGBA")
arr = np.array(src)
alpha = arr[:, :, 3]

for name, rgb in [("mk-redsea-badge-white", (255, 255, 255)), ("mk-redsea-badge-black", (0, 0, 0))]:
    out = np.zeros_like(arr)
    out[:, :, 0] = rgb[0]
    out[:, :, 1] = rgb[1]
    out[:, :, 2] = rgb[2]
    out[:, :, 3] = alpha
    img = Image.fromarray(out, mode="RGBA")

    # trim to content + resize to a reasonable web size, same as the color logo
    ys, xs = np.where(alpha > 10)
    pad = 20
    x0, x1 = max(xs.min() - pad, 0), min(xs.max() + pad, arr.shape[1])
    y0, y1 = max(ys.min() - pad, 0), min(ys.max() + pad, arr.shape[0])
    img = img.crop((x0, y0, x1, y1))

    max_dim = 1000
    w, h = img.size
    scale = min(1.0, max_dim / max(w, h))
    if scale < 1.0:
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

    out_path = OUT_DIR + name + ".png"
    img.save(out_path)
    print(f"wrote {out_path} {img.size}")
