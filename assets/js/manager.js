const logoutEl = document.querySelector("#logoutEl");

window.addEventListener('load', verifyToken('Employee'));

logoutEl.addEventListener("click", logout);