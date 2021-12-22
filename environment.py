from behave.runner import Context
from selenium import webdriver
from page_object_model.home_page import HomePage
from page_object_model.employee_page import EmployeePage
from page_object_model.manager_page import ManagerPage


def before_all(context: Context):
    context.driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.10/bin/chromedriver")
    context.home_page = HomePage(context.driver)
    context.employee_page = EmployeePage(context.driver)
    context.manager_page = ManagerPage(context.driver)


def after_all(context):
    context.driver.quit()
