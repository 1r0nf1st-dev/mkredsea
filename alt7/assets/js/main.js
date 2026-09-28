// Single source of truth for the Instagram DM link — update here only.
const INSTAGRAM_URL = "https://instagram.com/mootazkafii";

document.querySelectorAll('[data-instagram-cta]').forEach((el) => {
  el.href = INSTAGRAM_URL;
  el.target = "_blank";
  el.rel = "noopener";
});

document.getElementById('year').textContent = new Date().getFullYear();

// Mobile menu
const menuBtn = document.getElementById('menuBtn');
const nav = document.getElementById('nav');

function setMenu(open) {
  nav.classList.toggle('open', open);
  menuBtn.setAttribute('aria-expanded', String(open));
}

menuBtn.addEventListener('click', () => setMenu(!nav.classList.contains('open')));
nav.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => setMenu(false)));
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });

// Phone-only DM bar: slide it in once the hero's own buttons have scrolled away.
const mobileBar = document.querySelector('.mobile-bar');
const heroActions = document.querySelector('.hero-actions');
if (mobileBar && heroActions && 'IntersectionObserver' in window) {
  new IntersectionObserver(([entry]) => {
    mobileBar.classList.toggle('show', !entry.isIntersecting && entry.boundingClientRect.top < 0);
  }).observe(heroActions);
} else if (mobileBar) {
  mobileBar.classList.add('show');
}
