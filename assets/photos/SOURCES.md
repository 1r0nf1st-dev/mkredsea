# Photo sources

Stock photos (about + courses) are the same ones used on `/alt` (see `alt/assets/photos/SOURCES.md`), copied here as their
natural-color originals (not the blue-gray graded versions) to match the main site's
brighter palette. All from Unsplash under the [Unsplash License](https://unsplash.com/license)
(free for commercial and non-commercial use, no permission needed).

| File | Photographer | Source |
|---|---|---|
| about.jpg | Laya Clode | https://unsplash.com/photos/AwfxsOAkHXI |
| course-discovery.jpg | Uber Scuba Gili | https://unsplash.com/photos/bUQN08cphno |
| course-specialty.jpg | Simon Infanger | https://unsplash.com/photos/cB9-cyRU6aA |
| course-divemaster.jpg | Stanislav Stelmakhovich | https://unsplash.com/photos/mNSCo1Od8g8 |

## Client photos (hero + gallery)

`hero.jpg` and everything in `gallery/` are the client's own Red Sea photos, supplied
directly (not stock). The untouched files as received are kept in
`/assets/photos/originals/`; `scripts/process-photos.py` colour-corrects them (removes
the underwater blue cast / haze, restores contrast and warm tones), resizes them and
writes the web copies — a full-size `<name>.jpg` plus an 800px `<name>-800.jpg` for
phones. `hero.jpg` is the corrected `snapper-school` shot.
