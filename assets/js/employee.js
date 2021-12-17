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
getData(url);

// Get all categories 
let categoryUrl = 'http://127.0.0.1:5000/categories';
fetch(categoryUrl).then(res => res.json()).then(data => addCategories(data));


// Get all managers
let managersUrl = 'http://127.0.0.1:5000/managers';
getData(managersUrl);


// Logout event listener
logoutEl.addEventListener("click", logout);
formEl.addEventListener("submit", (e) =>{
    e.preventDefault();
    createObject();
    
});