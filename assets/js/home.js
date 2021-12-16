const formEl = document.querySelector("#loginForm");

function validateLogin(e) {
  e.preventDefault();

  console.log("Form was submitted");
}

formEl.addEventListener("submit", validateLogin);
