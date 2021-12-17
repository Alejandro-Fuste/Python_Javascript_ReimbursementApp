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

// Logout event listener
logoutEl.addEventListener("click", logout);
formEl.addEventListener("submit", (e) =>{
    e.preventDefault();
    validateUserInput();
    
});