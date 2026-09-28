# Photo sources

All photos are from Unsplash under the [Unsplash License](https://unsplash.com/license)
(free for commercial and non-commercial use, no permission needed). Credited here
even though attribution isn't required.

| File | Photographer | Source |
|---|---|---|
| about.jpg | Laya Clode | https://unsplash.com/photos/AwfxsOAkHXI |
| course-discovery.jpg | Uber Scuba Gili | https://unsplash.com/photos/bUQN08cphno |
| course-specialty.jpg | Simon Infanger | https://unsplash.com/photos/cB9-cyRU6aA |
| course-divemaster.jpg | Stanislav Stelmakhovich | https://unsplash.com/photos/mNSCo1Od8g8 |

The `*-raw.jpg` files are the unedited originals as downloaded; `grade-photos.py`
reads those and writes the blue-gray duotone versions actually used on the site
(`hero.jpg`, `about.jpg`, etc.) — re-run it if the grade ever needs adjusting.

## Client photos (hero + gallery)

`hero.jpg` and everything in `gallery/` are the client's own Red Sea photos, supplied
directly (not stock). The untouched files as received are kept in
`/assets/photos/originals/`; `scripts/process-photos.py` colour-corrects them (removes
the underwater blue cast / haze, restores contrast and warm tones), resizes them and
writes the web copies — a full-size `<name>.jpg` plus an 800px `<name>-800.jpg` for
phones. `hero.jpg` is the corrected `snapper-school` shot.

The alts' `hero.jpg` and `gallery/` photos are the same client photos, run through the
duotone grade by `scripts/grade-photos.py` (`hero-raw.jpg` is a copy of the main site's
colour-corrected hero; the gallery is graded straight from `/assets/photos/gallery/`).
