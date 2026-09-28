// Single source of truth for the Instagram DM link — update here only.
const INSTAGRAM_URL = "https://instagram.com/mootazkafii";

document.querySelectorAll('[data-instagram-cta]').forEach((el) => {
  el.href = INSTAGRAM_URL;
  el.target = "_blank";
  el.rel = "noopener";
});

document.getElementById('year').textContent = new Date().getFullYear();

// Depth gauge: each section declares its depth (data-depth). The reading is
// interpolated between the section tops either side of a line just under
// the top bar, so it matches a section's depth tag as that tag scrolls up.
const sections = [...document.querySelectorAll('[data-depth]')];
const maxDepth = Number(sections[sections.length - 1].dataset.depth);
const depthEl = document.getElementById('depth');
const fillEl = document.querySelector('.gauge-fill');
const PROBE_OFFSET = 120; // px from the top of the screen
let ticking = false;

function updateDepth() {
  const probe = window.scrollY + PROBE_OFFSET;
  const atBottom = window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2;
  let depth = 0;
  if (window.scrollY <= 0) {
    depth = 0;
  } else if (atBottom) {
    depth = maxDepth;
  } else {
    for (let i = 0; i < sections.length; i++) {
      const top = sections[i].offsetTop;
      const next = sections[i + 1];
      if (probe < top) break;
      const d = Number(sections[i].dataset.depth);
      if (!next) { depth = d; break; }
      const t = Math.min(1, (probe - top) / (next.offsetTop - top));
      depth = d + t * (Number(next.dataset.depth) - d);
    }
  }
  depthEl.textContent = Math.round(depth);
  fillEl.style.height = (depth / maxDepth * 100) + '%';
  ticking = false;
}

window.addEventListener('scroll', () => {
  if (!ticking) {
    requestAnimationFrame(updateDepth);
    ticking = true;
  }
}, { passive: true });
window.addEventListener('resize', updateDepth);
updateDepth();
