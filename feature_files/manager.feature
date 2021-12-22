Feature: Managers should be able to login, view, and update reimbursements

Scenario: as an Manager I want to view my reimbursements so I can see their status
    Given the Manager is on the login page
    When the Manager inputs their username into the username bar
    When the Manager inputs their password into the password bar
    When the Manager selects the user role
    When the Manager clicks the submit button
    Then the Manager should be sent to their webpage


Scenario: as a Manager, I want to view pending reimbursement so I approve or deny them
  Given I am on the manager page
  When I click the pending tab
  When I click the pending button
  When I enter the date
  When I select a status
  When I enter the reason
  When I click the save changes button
  Then I should see a success message