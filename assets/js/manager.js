// Logout button selector
const logoutEl = document.querySelector("#logoutEl");

// Event listener to prevent employees from accessing manager page
window.addEventListener('load', verifyToken('Employee'));

// Url for get all reimbursements
const url = `http://127.0.0.1:5000/reimbursements/all`

// Get all reimbursements 
getData(url);

// Logout event listener
logoutEl.addEventListener("click", logout);