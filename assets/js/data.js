const getData = async (url) => {
  const response = await fetch(url);

  let data = await response.json();

  console.log(data);
  return data;
};

const getName = () => {
  let tokenData = getToken();
  return `${tokenData["firstName"]} ${tokenData["lastName"]}`;
};

const addCategories = (data) => {
    const selectEl = document.querySelector('#validationCustom04');
     
    data.forEach((c) => {
        let createTag = document.createElement('option');
        createTag.textContent = c.categoryName;
        selectEl.appendChild(createTag);
    })
}

const addManagers = (data) => {
    const selectEl = document.querySelector('#validationCustom05');
    console.log(data)
    data.forEach((c) => {
        let createTag = document.createElement('option');
        createTag.setAttribute('data-id', c.managerId);
        createTag.textContent = `${c['firstName']} ${c['lastName']}`;
        selectEl.appendChild(createTag);
    })
}

// validate values for reimbursement
const validateUserInput = () => {
  let inputs = document.querySelectorAll("input");
  let selects = document.querySelectorAll("select");
  let validate = [...inputs, ...selects];
  let validated = {};

  validate.forEach((c) => {
      console.log()
    if (c.value === "" || c.value <= 0) {
      c.style.borderColor = "red";
      c.nextElementSibling.style.display = 'block';
    } else if (c.dataset.name === 'managerId') {
        validated[c.dataset.name] = parseInt(document.querySelector('[data-id]').dataset.id);
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
    object["employeeId"] = JSON.parse(localStorage.getItem('pseudoToken')).employeeId;
    

   console.table(object);
   return object
}
