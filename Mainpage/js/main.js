/*header*/
const searchBtn = document.querySelector('.navbar-searchBtn');
const toggleBtn = document.querySelector('.navbar-toggleBtn');
const menu = document.querySelector('.cover-navbar-menu');

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
});

searchBtn.addEventListener("click", () => {
    alert("search!!");
});

/*main*/
const backBtn = document.querySelector('.back-btn');
const generalBtn = document.querySelector('.general-btn');
const counselorBtn = document.querySelector('.counselor-btn');
const loginBtn = document.querySelector('.login-btn');

const searchIdBtn = document.querySelector('.search-id-btn');
const searchPasswordBtn = document.querySelector('.search-password-btn');
const joinBtn = document.querySelector('.join-btn');

const naverBtn = document.querySelector('.naver-btn');

backBtn.addEventListener('click', () => {
    alert("back!!");
});

generalBtn.addEventListener('click', () => {
    alert("general!!");
});

counselorBtn.addEventListener('click', () => {
    alert("counselor!!");
});

loginBtn.addEventListener('click', () => {
    alert("login!!");
});

searchIdBtn.addEventListener('click', () => {
    alert("searchId!!");
});

searchPasswordBtn.addEventListener('click', () => {
    alert("searchPassword!!");
});

joinBtn.addEventListener('click', () => {
    alert("join!!");
});

naverBtn.addEventListener('click', () => {
    alert("goNaver!!");
});
