from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "userName")
        return element

    def select_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "password")
        return element

    def select_role_dropdown(self):
        select_element = self.driver.find_element(By.ID, 'role')
        select_object = Select(select_element)
        select_object.select_by_value('employee')
        first_selected_option = select_object.first_selected_option
        return first_selected_option

    def select_submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submitButton")
        return element
