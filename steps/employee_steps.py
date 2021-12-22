from behave import Given, When, Then
import time


@Given(u'the employee is on the login page')
def get_login_page(context):
    context.driver.get("http://127.0.0.1:5500/home.html")


@When(u'the employee inputs their username into the username bar')
def enter_username(context):
    context.home_page.select_username_input().send_keys('NinjaCatGirl')


@When(u'the employee inputs their password into the password bar')
def enter_password(context):
    context.home_page.select_password_input().send_keys('JakkuJedi1')


@When(u'the employee selects the user role')
def select_role(context):
    context.home_page.select_role_dropdown().click()


@When(u'the employee clicks the submit button')
def click_submit_button(context):
    context.home_page.select_submit_button().click()


@Then(u"the employee should be sent to their webpage")
def check_employee_title(context):
    time.sleep(2)
    title = context.driver.title
    assert title == "Employee"


@Given(u'I am on the employee page')
def get_employee_page(context):
    context.driver.get("http://127.0.0.1:5500/employee.html")


@When(u'I enter the reimbursement date')
def enter_reimbursement_date(context):
    context.employee_page.select_reimbursement_date().send_keys('12222021')


@When(u'I enter the reimbursement amount')
def enter_reimbursement_amount(context):
    context.employee_page.select_reimbursement_amount().send_keys('600.45')


@When(u'I enter the reason for the reimbursement')
def enter_reimbursement_reason(context):
    context.employee_page.select_reimbursement_reason().send_keys('Spent money for gas')


@When(u'I select a category')
def select_category(context):
    context.employee_page.select_category_dropdown().click()
    time.sleep(1)


@When(u'I select my manager')
def select_manager(context):
    context.employee_page.select_manager_dropdown().click()
    time.sleep(1)


@When(u'I click the submit form button')
def click_submit_form_2(context):
    context.employee_page.select_submit_form_button().click()
    time.sleep(1)


@Then(u'I should see an alert message')
def alert_message(context):
    time.sleep(2)
    assert context.driver.switch_to.alert.text == "Your reimbursement was created."
    context.driver.switch_to.alert.accept()
