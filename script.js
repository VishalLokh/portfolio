document.getElementById('year').textContent = new Date().getFullYear();

const navToggle = document.getElementById('navToggle');
const navLinks = document.querySelector('.nav__links');

navToggle.addEventListener('click', () => {
  navLinks.classList.toggle('nav__links--open');
});

document.querySelectorAll('.nav__links a').forEach((link) => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('nav__links--open');
  });
});
