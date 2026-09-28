// Single source of truth for the Instagram DM link — update here only.
const INSTAGRAM_URL = "https://instagram.com/mootazkafii";

document.querySelectorAll('[data-instagram-cta]').forEach((el) => {
  el.href = INSTAGRAM_URL;
  el.target = "_blank";
  el.rel = "noopener";
});

document.getElementById('year').textContent = new Date().getFullYear();

// Dock the DM button to the bottom of the screen once the intro's own
// buttons have scrolled out of view.
const dock = document.querySelector('.dock');
const actions = document.querySelector('.actions');
if (dock && actions && 'IntersectionObserver' in window) {
  new IntersectionObserver(([entry]) => {
    dock.classList.toggle('show', !entry.isIntersecting && entry.boundingClientRect.top < 0);
  }).observe(actions);
}
