const getData = async (url) => {
  const response = await fetch(url);

  let data = await response.json();

  console.log(data);
};

const getName = () => {
  let tokenData = getToken();
  return `${tokenData["firstName"]} ${tokenData["lastName"]}`;
};

// validate values for reimbursement
const validateUserInput = () => {
  let inputs = document.querySelectorAll("input");
  let selects = document.querySelectorAll("select");
  let validate = [...inputs, ...selects];
  let validated = {};

  validate.forEach((c) => {
    if (c.value === "" || c.value <= 0) {
      c.style.borderColor = "red";
      c.nextElementSibling.style.display = 'block';
    } else if (c.value > 0) {
        validated[c.dataset.name] = parseFloat(c.value);
    } else {
        validated[c.dataset.name] = c.value.trim();
    }
  });
  
  return validated;
};

const createObject = () => {
    //values user entered into form
   let object = validateUserInput();

    // the rest of the values needed to create new reimbursment
    object["reimbursementId"] = 0;
    object["status"] = "pending";
    object["decisionDate"] = "null";
    object["reason"] = "null";
    object["employeeId"] = 3;
    object["managerId"] = 3;

   console.table(object);
}
