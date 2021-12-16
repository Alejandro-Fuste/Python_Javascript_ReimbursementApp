const login = (data) => {
  // send data retrieve from database to localStorage
  localStorage.setItem("pseudoToken", JSON.stringify(data));

  // redirect user base the role property in data
  const expr = data.companyRole;
  switch (expr) {
    case "Employee":
      window.location.assign("/employee.html");
      break;
    case "Manager":
      window.location.assign("/manager.html");
      break;
    default:
      errorEl.setAttribute("id", "errorMessage");
      errorEl.textContent = "Something went wrong...refresh and try again!";
  }
};

const validateCredentials = async (e) => {
  e.preventDefault();

  const errorEl = document.querySelector("#hideErrorMessage");

  let userName = document.querySelector("#userName").value;
  let userPassword = document.querySelector("#password").value;

  let loginData = {
    userName,
    userPassword,
  };

  const response = await fetch("http://127.0.0.1:5000/employee", {
    method: "POST",
    mode: "cors",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(loginData),
  });

  if (response.status === 200) {
    let content = await response.json();
    login(content);
  } else {
    let content = await response.json();
    errorEl.setAttribute("id", "errorMessage");
    errorEl.textContent = content.message;
  }
};
