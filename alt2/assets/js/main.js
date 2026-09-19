// Single source of truth for the Instagram DM link — update here only.
const INSTAGRAM_URL = "https://instagram.com/mootazkafii";

document.querySelectorAll('[data-instagram-cta]').forEach((el) => {
  el.href = INSTAGRAM_URL;
  el.target = "_blank";
  el.rel = "noopener";
});

document.getElementById('year').textContent = new Date().getFullYear();

// Theme toggle, persisted in localStorage
const root = document.documentElement;
const themeToggle = document.getElementById('themeToggle');

function applyTheme(theme) {
  if (theme === 'dark') {
    root.setAttribute('data-theme', 'dark');
  } else {
    root.setAttribute('data-theme', 'light');
  }
}

try {
  const saved = localStorage.getItem('mkredsea-theme');
  if (saved) applyTheme(saved);
} catch (e) {}

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const isDark = root.getAttribute('data-theme') === 'dark';
    const next = isDark ? 'light' : 'dark';
    applyTheme(next);
    try { localStorage.setItem('mkredsea-theme', next); } catch (e) {}
  });
}

// Full-screen nav overlay
const navToggle = document.getElementById('navToggle');
const navOverlay = document.getElementById('navOverlay');
const navClose = document.getElementById('navClose');

function openNav() {
  navOverlay.classList.add('open');
  navToggle.setAttribute('aria-expanded', 'true');
}
function closeNav() {
  navOverlay.classList.remove('open');
  navToggle.setAttribute('aria-expanded', 'false');
}

if (navToggle && navOverlay) {
  navToggle.addEventListener('click', openNav);
  navClose.addEventListener('click', closeNav);
  navOverlay.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeNav);
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeNav();
  });
}
