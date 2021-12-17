// Event listener to prevent managers from accessing employee page
window.addEventListener('load', verifyToken('Manager'));

// Logout and employee name selectors
const logoutEl = document.querySelector("#logoutEl");
const nameEl = document.querySelector('#employeeName');
const formEl = document.querySelector('#reimbursementForm');

// Add name to element
nameEl.textContent = getName();


// Get id from local storage and add it to url for get all employee reimbursements
let tokenData = getToken();
let id = tokenData['employeeId']
let url = `http://127.0.0.1:5000/reimbursements/${id}`;

// Get all employee reimbursements 
getData(url);



// Logout event listener
logoutEl.addEventListener("click", logout);
formEl.addEventListener("submit", (e) =>{
    e.preventDefault();
    validateUserInput();
    
});