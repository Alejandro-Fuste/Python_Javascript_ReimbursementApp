from behave import Given, When, Then
import time


@Given(u'the user is on the login page')
def get_login_page(context):
    context.driver.get("http://127.0.0.1:5500/home.html")


@When(u'the user inputs their username into the username bar')
def enter_username(context):
    context.home_page.select_username_input().send_keys('NinjaCatGirl')


@When(u'the user inputs their password into the password bar')
def enter_password(context):
    context.home_page.select_password_input().send_keys('JakkuJedi1')


@When(u'the user selects the user role')
def select_role(context):
    context.home_page.select_role_dropdown().click()


@When(u'the user clicks the submit button')
def click_submit_button(context):
    context.home_page.select_submit_button().click()


@Then(u"the user should be sent to their webpage")
def check_employee_title(context):
    time.sleep(2)
    title = context.driver.title
    assert title == "Employee"
