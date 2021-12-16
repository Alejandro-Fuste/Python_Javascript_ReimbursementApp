const sendtoLocalStorage = (data) => {
  console.table(data);
};

const validateLogin = async (e) => {
  e.preventDefault();

  let userName = document.querySelector("#userName").value;
  let userPassword = document.querySelector("#password").value;

  let loginData = {
    userName,
    userPassword,
  };

  sendtoLocalStorage(loginData);

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
