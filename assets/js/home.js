const formEl = document.querySelector("#loginForm");

function validateLogin(e) {
  e.preventDefault();

  let userName = document.querySelector("#userName").value;
  let password = document.querySelector("#password").value;

  console.table(userName, password);
}

formEl.addEventListener("submit", validateLogin);
