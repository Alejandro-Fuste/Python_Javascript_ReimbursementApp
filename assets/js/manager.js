// Event listener to prevent employees from accessing manager page
window.addEventListener('load', verifyToken('Employee'));

// Logout and manager name selectors
const logoutEl = document.querySelector("#logoutEl");
const nameEl = document.querySelector('#managerName');

// Add name to element
nameEl.textContent = getName();


// Url for get all reimbursements
const url = `http://127.0.0.1:5000/reimbursements/all`

// Get all reimbursements 
getData(url);

// Logout event listener
logoutEl.addEventListener("click", logout);