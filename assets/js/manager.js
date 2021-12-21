// Event listener to prevent employees from accessing manager page
window.addEventListener('load', verifyToken('Employee'));

// Logout and manager name selectors
const logoutEl = document.querySelector("#logoutEl");
const nameEl = document.querySelector('#managerName');
const allEl = document.querySelector('#allButton');
const approvedEl = document.querySelector('#approvedButton');
const deniedEl = document.querySelector('#deniedButton');
const pendingEl = document.querySelector('#pendingButton');
const empEl = document.querySelector("#employeeSelect");
const categoryEl = document.querySelector('#categorySelect');
// let updateObj = {};

// Add name to element
nameEl.textContent = getName();

// Get all reimbursements 
const url = `http://127.0.0.1:5000/reimbursements/all`;
fetch(url).then(res => res.json()).then(data => addReimbursementsManager(data)).catch(err => errorAlert);

// Get total reimbursement
const totalUrl = `http://127.0.0.1:5000/reimbursements/total`;
fetch(totalUrl).then(res => res.json()).then(data => displayTotalReimbursements(data)).catch(err => errorAlert)

// Get rejected total
const rejectUrl = `http://127.0.0.1:5000/reimbursements/rejected`;
fetch(rejectUrl).then(res => res.json()).then(data => displayRejectedAmount(data)).catch(err => errorAlert);

// Get top five spenders 
const topUrl = `http://127.0.0.1:5000/reimbursements/topFive`
fetch(topUrl).then(res => res.json()).then(data => displayTopSpenders(data)).catch(err => errorAlert);

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

// Get total reimbursement by employee
empEl.addEventListener('change', displayTotalReimbursementByEmployee);

// Get total reimbursement by category
categoryEl.addEventListener('change', displayTotalReimbursementByCategory);

// Change status of reimbursement
document.addEventListener('click',function(e){
    if(e.target && e.target.id == 'changeStatusButton'){

          let object = {};

          object['reimbursementId'] = e.target.dataset.id;
          object['reimbursementAmount'] = e.target.dataset.amount;
          object["category"] = e.target.dataset.category;
          object["reimbursementReason"] = e.target.dataset.reimbursementreason;
          object["reimbursementDate"] = e.target.dataset.reimbursementdate;
          object["employeeId"] = e.target.dataset.employeeid;
          object["managerId"] = e.target.dataset.managerid;

        localStorage.setItem('updateObj', JSON.stringify(object))
        
     }
 });


