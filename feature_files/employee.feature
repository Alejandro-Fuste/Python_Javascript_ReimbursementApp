Feature: Employees should be able to login, view, and create a new reimbursement

Scenario: as an Employee, I want to login so I can see my reimbursements
    Given the Employee is on the login page
    When the Employee inputs their username into the username bar
    When the Employee inputs their password into the password bar
    When the Employee selects the user role
    When the Employee clicks the submit button
    Then the Employee should be sent to their webpage


Scenario: as an Employee, I want to create a new reimbursement so I can be reimbursed for the money I spent
  Given I am on the employee page
  When I enter the reimbursement date
  When I enter the reimbursement amount
  When I enter the reason for the reimbursement
  When I select a category
  When I select my manager
  When I click the submit form button
  Then I should see an alert message