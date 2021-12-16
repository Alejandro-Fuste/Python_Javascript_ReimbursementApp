const login = (data) => {
  // send data retrieve from database to localStorage
  localStorage.setItem("pseudoToken", JSON.stringify(data));

  // redirect user base the role property in data
  const expr = "Employee";
  switch (expr) {
    case "Employee":
      console.log("Employee");
      break;
    case "Manager":
      console.log("Manager");
      break;
    default:
      console.log(`Sorry, we are out of ${expr}.`);
  }
};

const validateCredentials = async (e) => {
  e.preventDefault();

  let userName = document.querySelector("#userName").value;
  let userPassword = document.querySelector("#password").value;

  let loginData = {
    userName,
    userPassword,
  };

  login(loginData);

  // const response = await fetch("http://127.0.0.1:5000/employee", {
  //   method: "POST",
  //   mode: "cors",
  //   headers: {
  //     Accept: "application/json",
  //     "Content-Type": "application/json",
  //   },
  //   body: JSON.stringify(loginData),
  // });
  // const content = await response.json();

  // console.log(content);
};
