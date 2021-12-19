// Event listener to prevent employees from accessing manager page
window.addEventListener('load', verifyToken('Employee'));

// Logout and manager name selectors
const logoutEl = document.querySelector("#logoutEl");
const nameEl = document.querySelector('#managerName');
const approvedEl = document.querySelector('#approvedButton')

// Add name to element
nameEl.textContent = getName();


// Get all reimbursements 
const url = `http://127.0.0.1:5000/reimbursements/all`
fetch(url).then(res => res.json()).then(data => addReimbursementsManager(data)).catch(err => console.log(error));

// Approved button event listener
approvedEl.addEventListener('click', approvedButtonDisplay);

// Logout button event listener
logoutEl.addEventListener("click", logout);