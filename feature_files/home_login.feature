Feature: Application should have different role pages

  Scenario: as an User I want to view my reimbursements so I can see their status
    Given the user is on the login page
    When the user inputs their username into the username bar
    When the user inputs their password into the password bar
    When the user selects the user role
    When the user clicks the submit button
    Then the user should be sent to their webpage
