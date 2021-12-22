from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class EmployeePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_reimbursement_date(self):
        element: WebElement = self.driver.find_element(By.ID, "validationCustom01")
        return element

    def select_reimbursement_amount(self):
        element: WebElement = self.driver.find_element(By.ID, "validationCustom02")
        return element

    def select_reimbursement_reason(self):
        element: WebElement = self.driver.find_element(By.ID, "validationCustom03")
        return element

    def select_category_dropdown(self):
        select_element = self.driver.find_element(By.ID, 'validationCustom04')
        select_object = Select(select_element)
        select_object.select_by_visible_text('Gas')
        first_selected_option = select_object.first_selected_option
        return first_selected_option

    def select_manager_dropdown(self):
        select_element = self.driver.find_element(By.ID, 'validationCustom05')
        select_object = Select(select_element)
        select_object.select_by_visible_text('Luke Skywalker')
        first_selected_option = select_object.first_selected_option
        return first_selected_option

    def select_submit_form_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submitButton2")
        return element



