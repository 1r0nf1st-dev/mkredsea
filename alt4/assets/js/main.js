// Single source of truth for the Instagram DM link — update here only.
const INSTAGRAM_URL = "https://instagram.com/mootazkafii";

document.querySelectorAll('[data-instagram-cta]').forEach((el) => {
  el.href = INSTAGRAM_URL;
  el.target = "_blank";
  el.rel = "noopener";
});

document.getElementById('year').textContent = new Date().getFullYear();
