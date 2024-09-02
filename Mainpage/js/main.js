const toggleBtn = document.querySelector('.navbar-toggleBtn');
const menu = document.querySelector('.navbar-menu');

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
});