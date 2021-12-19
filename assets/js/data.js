// const getData = async (url) => {
//   const response = await fetch(url);

//   let data = await response.json();

//   return data;
// };

const getName = () => {
  let tokenData = getToken();
  return `${tokenData["firstName"]} ${tokenData["lastName"]}`;
};

const addReimbursements = (data) => {
    const selectEl = document.querySelector('#reimbUl');

    data.forEach((c) => {
        let createLiTag = document.createElement('li');
        createLiTag.setAttribute('id', 'reimLi');

        let createDivTag = document.createElement('div');
        createDivTag.setAttribute('id', 'reimDiv');

        let createIdTag = document.createElement('p');
        createIdTag.setAttribute('id', 'reimP');
        createIdTag.textContent = c.reimbursementId;

        let createStatusTag = document.createElement('p');
        createStatusTag.setAttribute('id', 'reimP');
        createStatusTag.textContent = c.status;

        let createDateTag = document.createElement('p');
        createDateTag.setAttribute('id', 'reimP');
        createDateTag.textContent = c.reimbursementDate;

        let createCategoryTag = document.createElement('p');
        createCategoryTag.setAttribute('id', 'reimP');
        createCategoryTag.textContent = c.category;

        let createAmountTag = document.createElement('p');
        createAmountTag.setAttribute('id', 'reimP');
        createAmountTag.textContent = c.reimbursementAmount;

        let createReimbursementReasonTag = document.createElement('p');
        createReimbursementReasonTag.setAttribute('id', 'reimP');
        createReimbursementReasonTag.textContent = c.reimbursementReason;

        let createDecisionDateTag = document.createElement('p');
        createDecisionDateTag.setAttribute('id', 'reimP');
        createDecisionDateTag.textContent = c.decisionDate;

        let createReasonTag = document.createElement('p');
        createReasonTag.setAttribute('id', 'reimP');
        createReasonTag.textContent = c.reason;

        createDivTag.append(createIdTag, createStatusTag, createDateTag, createCategoryTag, createAmountTag, createReimbursementReasonTag, createDecisionDateTag, createReasonTag);
        createLiTag.appendChild(createDivTag);
        selectEl.appendChild(createLiTag);
    })
};

const addCategories = (data) => {
    const selectEl = document.querySelector('#validationCustom04');
     
    data.forEach((c) => {
        let createTag = document.createElement('option');
        createTag.textContent = c.categoryName;
        selectEl.appendChild(createTag);
    })
};

const addManagers = (data) => {
    const selectEl = document.querySelector('#validationCustom05');
    
    data.forEach((c) => {
        let createTag = document.createElement('option');
        createTag.setAttribute('data-id', c.managerId);
        createTag.textContent = `${c['firstName']} ${c['lastName']}`;
        selectEl.appendChild(createTag);
    })
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

// object holding data for creating reimbursement
const createObject = () => {
    //values user entered into form
   let object = validateUserInput();

    // the rest of the values needed to create new reimbursment
    object["reimbursementId"] = 0;
    object["status"] = "pending";
    object["decisionDate"] = "null";
    object["reason"] = "null";
    object["employeeId"] = JSON.parse(localStorage.getItem('pseudoToken')).employeeId;
    
   return object
};

// send data to create reimbursement
const createReimbursement = async (url,data) => {
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
    
      if (response.status === 201) {
        let content = await response.json();
        alert('Your reimbursement was created.');
      } else {
        let content = await response.json();
        alert(content.message);
    
      }
};
