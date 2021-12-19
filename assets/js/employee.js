// Event listener to prevent managers from accessing employee page
window.addEventListener('load', verifyToken('Manager'));

// Logout and employee name selectors
const logoutButtonEl = document.querySelector("#logoutEl");
const nameEl = document.querySelector('#employeeName');
const reimbursementFormEl = document.querySelector('#reimbursementForm');

// Add name to element
nameEl.textContent = getName();


// Get id from local storage and add it to url for get all employee reimbursements
let tokenData = getToken();
let id = tokenData['employeeId']
let reimbursementsUrl = `http://127.0.0.1:5000/reimbursements/${id}`;
// getData(url);
fetch(reimbursementsUrl).then(res => res.json()).then(data => addReimbursements(data)).catch(err => console.log(err));

// Get all categories 
let categoryUrl = 'http://127.0.0.1:5000/categories';
fetch(categoryUrl).then(res => res.json()).then(data => addCategories(data)).catch(err => console.log(err));


// Get all managers
let managersUrl = 'http://127.0.0.1:5000/managers';
fetch(managersUrl).then(res => res.json()).then(data => addManagers(data)).catch(err => console.log(err));


// Logout event listener
logoutButtonEl.addEventListener("click", logout);
reimbursementFormEl.addEventListener("submit", (e) =>{
    e.preventDefault();

    let reimbursementUrl = 'http://127.0.0.1:5000/reimbursement';
    let data = createObject();

    createReimbursement(reimbursementUrl, data);
    
});