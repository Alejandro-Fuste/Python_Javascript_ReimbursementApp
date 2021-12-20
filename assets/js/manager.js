// Event listener to prevent employees from accessing manager page
window.addEventListener('load', verifyToken('Employee'));

// Logout and manager name selectors
const logoutEl = document.querySelector("#logoutEl");
const nameEl = document.querySelector('#managerName');
const allEl = document.querySelector('#allButton');
const approvedEl = document.querySelector('#approvedButton');
const deniedEl = document.querySelector('#deniedButton');
const pendingEl = document.querySelector('#pendingButton');

// Add name to element
nameEl.textContent = getName();


// Get all reimbursements 
const url = `http://127.0.0.1:5000/reimbursements/all`
fetch(url).then(res => res.json()).then(data => addReimbursementsManager(data)).catch(err => alert("Opps, something is wrong with the server connection"));

// All button event listener
allEl.addEventListener('click', allButtonDisplay);

// Approved button event listener
approvedEl.addEventListener('click', approvedButtonDisplay);

// Denied button event listener
deniedEl.addEventListener('click', deniendButtonDisplay);

// Pending button event listener
pendingEl.addEventListener('click', pendingButtonDisplay);

// Logout button event listener
logoutEl.addEventListener("click", logout);