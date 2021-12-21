const errorAlert = () =>
  alert("Opps, something is wrong with the server connection");

const getName = () => {
  let tokenData = getToken();
  return `${tokenData["firstName"]} ${tokenData["lastName"]}`;
};

const approveDenyReimbursement = async () => {
  let object = JSON.parse(localStorage.getItem("updateObj"));
  const url = `http://127.0.0.1:5000/reimbursements`

  const dateEl = document.querySelector("#validationCustom01");
  const statusEl = document.querySelector("#validationCustom02");
  const reasonEl = document.querySelector("#validationCustom03");
  const inputArray = [dateEl, statusEl, reasonEl];

  inputArray.forEach((c) => {
    if (c.value === "" || c.value <= 0 || typeof c.value === "number") {
      c.style.borderColor = "red";
      c.nextElementSibling.style.display = "block";
    } else {
      object["status"] = statusEl.value;
      object["reason"] = reasonEl.value;
      object["decisionDate"] = dateEl.value;
      console.table(object);
    }
  });

  const response = await fetch(url, {
      method: "PATCH",
      mode: "cors",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(object),
    });

    if (response.status === 200) {
      let content = await response.json();
      alert(content);
      location.reload();

    } else {
      let content = await response.json();
      alert(content.message);
    }
};

const addReimbursements = (data) => {
  const selectEl = document.querySelector("#reimbUl");

  data.forEach((c) => {
    let createLiTag = document.createElement("li");
    createLiTag.setAttribute("id", "reimLi");

    let createDivTag = document.createElement("div");
    createDivTag.setAttribute("id", "reimDiv");

    let createIdTag = document.createElement("p");
    createIdTag.setAttribute("id", "reimP");
    createIdTag.textContent = `Id: ${c.reimbursementId}`;

    let createStatusTag = document.createElement("p");
    createStatusTag.setAttribute("id", "reimP");
    createStatusTag.textContent = `Status: ${c.status}`;

    let createDateTag = document.createElement("p");
    createDateTag.setAttribute("id", "reimP");
    createDateTag.textContent = `Created Date: ${c.reimbursementDate}`;

    let createCategoryTag = document.createElement("p");
    createCategoryTag.setAttribute("id", "reimP");
    createCategoryTag.textContent = `Category: ${c.category}`;

    let createAmountTag = document.createElement("p");
    createAmountTag.setAttribute("id", "reimP");
    createAmountTag.textContent = `Amount: ${c.reimbursementAmount}`;

    let createReimbursementReasonTag = document.createElement("p");
    createReimbursementReasonTag.setAttribute("id", "reimP");
    createReimbursementReasonTag.textContent = `Reason for reimbursement: ${c.reimbursementReason}`;

    let createDecisionDateTag = document.createElement("p");
    createDecisionDateTag.setAttribute("id", "reimP");
    createDecisionDateTag.textContent = `Decision Date: ${c.decisionDate}`;

    let createReasonTag = document.createElement("p");
    createReasonTag.setAttribute("id", "reimP");
    createReasonTag.textContent = `Manager comment: ${c.reason}`;

    createDivTag.append(
      createIdTag,
      createStatusTag,
      createDateTag,
      createCategoryTag,
      createAmountTag,
      createReimbursementReasonTag,
      createDecisionDateTag,
      createReasonTag
    );
    createLiTag.appendChild(createDivTag);
    selectEl.appendChild(createLiTag);
  });
};

const addCategories = (data) => {
  const selectEl = document.querySelector("#validationCustom04");

  data.forEach((c) => {
    let createTag = document.createElement("option");
    createTag.textContent = c.categoryName;
    selectEl.appendChild(createTag);
  });
};

const addManagers = (data) => {
  const selectEl = document.querySelector("#validationCustom05");

  data.forEach((c) => {
    let createTag = document.createElement("option");
    createTag.setAttribute("data-id", c.managerId);
    createTag.textContent = `${c["firstName"]} ${c["lastName"]}`;
    selectEl.appendChild(createTag);
  });
};

const addReimbursementsManager = (data) => {
  const selectEl = document.querySelector("#reimbUL");

  data.forEach((c) => {
    let buttonDiv = document.createElement("div");

    let createLiTag = document.createElement("li");
    createLiTag.setAttribute("id", c.status);

    let createDivTag = document.createElement("div");
    createDivTag.setAttribute("id", "reimDiv");

    let createIdTag = document.createElement("p");
    createIdTag.setAttribute("id", "reimP");
    createIdTag.textContent = `Id: ${c.reimbursementId}`;

    if (c.status === "pending") {
      let createButton = document.createElement("button");
      createButton.setAttribute("type", "submit");
      createButton.setAttribute("class", "btn btn-primary");
      createButton.setAttribute("data-bs-toggle", "modal");
      createButton.setAttribute("data-bs-target", "#exampleModal");
      createButton.setAttribute("id", "changeStatusButton");
      createButton.setAttribute("data-id", c.reimbursementId);
      createButton.setAttribute("data-amount", c.reimbursementAmount);
      createButton.setAttribute("data-category", c.category);
      createButton.setAttribute(
        "data-reimbursementReason",
        c.reimbursementReason
      );
      createButton.setAttribute("data-reimbursementDate", c.reimbursementDate);
      createButton.setAttribute("data-status", c.status);
      createButton.setAttribute("data-decisionDate", c.decisionDate);
      createButton.setAttribute("data-reason", c.reason);
      createButton.setAttribute("data-employeeId", c.employeeId);
      createButton.setAttribute("data-managerId", c.managerId);
      createButton.textContent = "+";
      buttonDiv.append(createIdTag, createButton);
      createDivTag.append(buttonDiv);
    } else {
      createDivTag.append(createIdTag);
    }

    let createStatusTag = document.createElement("p");
    createStatusTag.setAttribute("id", "reimP");
    createStatusTag.textContent = `Status: ${c.status}`;

    let createDateTag = document.createElement("p");
    createDateTag.setAttribute("id", "reimP");
    createDateTag.textContent = `Created Date: ${c.reimbursementDate}`;

    let createCategoryTag = document.createElement("p");
    createCategoryTag.setAttribute("id", "reimP");
    createCategoryTag.textContent = `Category: ${c.category}`;

    let createAmountTag = document.createElement("p");
    createAmountTag.setAttribute("id", "reimP");
    createAmountTag.textContent = `Amount: ${c.reimbursementAmount}`;

    let createReimbursementReasonTag = document.createElement("p");
    createReimbursementReasonTag.setAttribute("id", "reimP");
    createReimbursementReasonTag.textContent = `Reason for reimbursement: ${c.reimbursementReason}`;

    let createDecisionDateTag = document.createElement("p");
    createDecisionDateTag.setAttribute("id", "reimP");
    createDecisionDateTag.textContent = `Decision Date: ${c.decisionDate}`;

    let createReasonTag = document.createElement("p");
    createReasonTag.setAttribute("id", "reimP");
    createReasonTag.textContent = `Manager comment: ${c.reason}`;

    createDivTag.append(
      createStatusTag,
      createDateTag,
      createCategoryTag,
      createAmountTag,
      createReimbursementReasonTag,
      createDecisionDateTag,
      createReasonTag
    );
    createLiTag.appendChild(createDivTag);
    selectEl.appendChild(createLiTag);
  });
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
      c.nextElementSibling.style.display = "block";
    } else if (c.dataset.name === "managerId") {
      validated[c.dataset.name] = parseInt(
        document.querySelector("[data-id]").dataset.id
      );
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
  object["employeeId"] = JSON.parse(
    localStorage.getItem("pseudoToken")
  ).employeeId;

  return object;
};

// send data to create reimbursement
const createReimbursement = async (url, data) => {
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
    alert("Your reimbursement was created.");
  } else {
    let content = await response.json();
    alert(content.message);
  }
};

const allButtonDisplay = () => {
  let liElements = document.querySelectorAll("li");
  let liArray = [...liElements];

  liArray.forEach((c) => (c.style.display = "block"));
};

const approvedButtonDisplay = () => {
  allButtonDisplay();
  let liElements = document.querySelectorAll("li");
  let liArray = [...liElements];
  let filtered = liArray.filter((c) => c.id != "approved");

  filtered.forEach((c) => (c.style.display = "none"));
};

const deniendButtonDisplay = () => {
  allButtonDisplay();
  let liElements = document.querySelectorAll("li");
  let liArray = [...liElements];
  let filtered = liArray.filter((c) => c.id != "rejected");

  filtered.forEach((c) => (c.style.display = "none"));
};

const pendingButtonDisplay = () => {
  allButtonDisplay();
  let liElements = document.querySelectorAll("li");
  let liArray = [...liElements];
  let filtered = liArray.filter((c) => c.id != "pending");

  filtered.forEach((c) => (c.style.display = "none"));
};

const displayTotalReimbursements = (data) => {
  let totalEl = document.querySelector("#totalAppReimb");
  totalEl.textContent = data.total;
};

const displayRejectedAmount = (data) => {
  const rejectEl = document.querySelector("#totalRejectReimb");
  rejectEl.textContent = data.total;
};

const displayTotalReimbursementByEmployee = () => {
  const empEl = document.querySelector("#employeeSelect").value;

  const totalEmpUrl = `http://127.0.0.1:5000/reimbursements/total/${empEl}`;

  fetch(totalEmpUrl)
    .then((res) => res.json())
    .then((data) => {
      let totalEl = document.querySelector("#totalEmpReimb");
      totalEl.textContent = data.total;
    })
    .catch((err) => errorAlert);
};

const displayTotalReimbursementByCategory = () => {
  const categoryEl = document.querySelector("#categorySelect").value;
  const url = `http://127.0.0.1:5000/reimbursements/total/category/${categoryEl}`;

  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      let totalEl = document.querySelector("#totalCatReimb");
      totalEl.textContent = data.total;
    })
    .catch((err) => errorAlert);
};

const displayTopSpenders = (data) => {
  const selectEl = document.querySelector("#spendersList");

  data.forEach((c) => {
    let buttonDiv = document.createElement("div");

    let createLiTag = document.createElement("li");
    createLiTag.setAttribute("id", c.status);

    let createDivTag = document.createElement("div");
    createDivTag.setAttribute("id", "reimDiv");

    let createIdTag = document.createElement("p");
    createIdTag.setAttribute("id", "reimP");
    createIdTag.textContent = `Id: ${c.reimbursementId}`;

    if (c.employeeId === 1) {
      let createButton = document.createElement("p");
      createButton.setAttribute("id", "reimP");
      createButton.textContent = `Employee: Rey Skywalker`;
      buttonDiv.append(createIdTag, createButton);
      createDivTag.append(buttonDiv);
    } else if (c.employeeId === 2) {
      let createButton = document.createElement("p");
      createButton.setAttribute("id", "reimP");
      createButton.textContent = `Employee: Ben Solo`;
      buttonDiv.append(createIdTag, createButton);
      createDivTag.append(buttonDiv);
    } else if (c.employeeId === 3) {
      let createButton = document.createElement("p");
      createButton.setAttribute("id", "reimP");
      createButton.textContent = `Employee: Admiral Ackbar`;
      buttonDiv.append(createIdTag, createButton);
      createDivTag.append(buttonDiv);
    }

    let createStatusTag = document.createElement("p");
    createStatusTag.setAttribute("id", "reimP");
    createStatusTag.textContent = `Status: ${c.status}`;

    let createDateTag = document.createElement("p");
    createDateTag.setAttribute("id", "reimP");
    createDateTag.textContent = `Created Date: ${c.reimbursementDate}`;

    let createCategoryTag = document.createElement("p");
    createCategoryTag.setAttribute("id", "reimP");
    createCategoryTag.textContent = `Category: ${c.category}`;

    let createAmountTag = document.createElement("p");
    createAmountTag.setAttribute("id", "reimP");
    createAmountTag.textContent = `Amount: ${c.reimbursementAmount}`;

    let createReimbursementReasonTag = document.createElement("p");
    createReimbursementReasonTag.setAttribute("id", "reimP");
    createReimbursementReasonTag.textContent = `Reason for reimbursement: ${c.reimbursementReason}`;

    let createDecisionDateTag = document.createElement("p");
    createDecisionDateTag.setAttribute("id", "reimP");
    createDecisionDateTag.textContent = `Decision Date: ${c.decisionDate}`;

    let createReasonTag = document.createElement("p");
    createReasonTag.setAttribute("id", "reimP");
    createReasonTag.textContent = `Manager comment: ${c.reason}`;

    createDivTag.append(
      createStatusTag,
      createDateTag,
      createCategoryTag,
      createAmountTag,
      createReimbursementReasonTag,
      createDecisionDateTag,
      createReasonTag
    );
    createLiTag.appendChild(createDivTag);
    selectEl.appendChild(createLiTag);
  });
};
