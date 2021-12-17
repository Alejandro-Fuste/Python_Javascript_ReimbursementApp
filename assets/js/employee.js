const logoutEl = document.querySelector("#logoutEl");

window.addEventListener('load', verifyToken('Manager'));

logoutEl.addEventListener("click", logout);