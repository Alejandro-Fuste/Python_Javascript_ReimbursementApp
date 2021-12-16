const functionsObject = {
  validateLogin: (e) => {
    e.preventDefault();

    let userName = document.querySelector("#userName").value;
    let password = document.querySelector("#password").value;

    console.table(userName, password);
  },
};
