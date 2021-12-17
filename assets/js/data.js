const getData = async (url) => {
  const response = await fetch(url);

  let data = await response.json();

  console.log(data);
};

const getName = () => {
  let tokenData = getToken();
  return `${tokenData["firstName"]} ${tokenData["lastName"]}`;
};

const validateUserInput = () => {
  let inputs = document.querySelectorAll("input");
  let selects = document.querySelectorAll("select");
  let amountInput = document.querySelector("#amountInput");
  let invalidEl = document.querySelector(".invalid-feedback");
  let validate = [...inputs, ...selects];

  validate.forEach((c) => {
    if (c.value === "" || c.value < 0) {
      c.style.borderColor = "red";
      c.nextElementSibling.style.display = 'block';
    }
  });

  if (typeof amountInput.value === "string") {
    amountInput.style.borderColor = "red";
    amountInput.nextElementSibling.style.display = "block";
  }
};
