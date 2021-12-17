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
      console.log(c.value);
      console.log(typeof(c.value));
    if (c.value === "" || c.value <= 0) {
      c.style.borderColor = "red";
      c.nextElementSibling.style.display = 'block';
    } else if (c.value > 0) {
        validated[c.dataset.name] = parseFloat(c.value);
    } else {
        validated[c.dataset.name] = c.value;
    }
  });

  console.table(validated);
};

// Create new reimbursement

    // get values from user (reimbursementAmount, category, reimbursementReason, reimbursementDate)
    // validate those values

    // set default value of 0 for reimbursementId
    // set default value of pending for status
    // set default value of null for decisionDate and reason 
    // enter ids for employee and manager

    /*{
        "reimbursementId": 10,
        "reimbursementAmount": "1000.00",
        "category": "Hotel",
        "reimbursementReason": "Hotel stay on Coruscant",
        "reimbursementDate": "12-15-2021",
        "status": "pending",
        "decisionDate": "null",
        "reason": "null",
        "employeeId": 3,
        "managerId": 1
    }*/