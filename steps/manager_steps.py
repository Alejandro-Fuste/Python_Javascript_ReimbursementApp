from behave import Given, When, Then
import time


@Given(u'the manager is on the login page')
def get_login_page(context):
    context.driver.get("http://127.0.0.1:5500/home.html")


@When(u'the manager inputs their username into the username bar')
def enter_username(context):
    context.home_page.select_username_input().send_keys('Master Jedi')


@When(u'the manager inputs their password into the password bar')
def enter_password(context):
    context.home_page.select_password_input().send_keys('TheRealChosenOne')


@When(u'the manager selects the user role')
def select_role(context):
    context.manager_page.select_manager_role_dropdown().click()


@When(u'the manager clicks the submit button')
def click_submit_button(context):
    context.home_page.select_submit_button().click()


@Then(u"the manager should be sent to their webpage")
def check_manager_title(context):
    time.sleep(2)
    title = context.driver.title
    assert title == "Manager"


@Given(u'I am on the manager page')
def get_manager_page(context):
    context.driver.get('http://127.0.0.1:5500/manager.html')
    time.sleep(3)


@When(u'I click the pending tab')
def click_pending_tab(context):
    context.manager_page.select_pending_tab().click()
    time.sleep(3)


@When(u'I click the pending button')
def click_pending_button(context):
    context.manager_page.select_pending_plus_button().click()
    time.sleep(3)


@When(u'I enter the date')
def click_date_button(context):
    context.manager_page.select_date().send_keys('12222021')


@When(u'I select a status')
def select_status(context):
    context.manager_page.select_status_from_dropdown().click()
    time.sleep(1)


@When(u'I enter the reason')
def input_reason(context):
    context.manager_page.select_reason_input().send_keys('Your reimbursement have been approved')


@When(u'I click the save changes button')
def click_save_changes_button(context):
    context.manager_page.select_save_changes_button().click()
    time.sleep(1)


@Then(u'I should see a success message')
def check_success_message(context):
    assert context.manager_page.select_success_message() == "Reimbursement was updated successfully."
