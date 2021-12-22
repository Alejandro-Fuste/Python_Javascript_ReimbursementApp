from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class ManagerPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_manager_role_dropdown(self):
        select_element = self.driver.find_element(By.ID, 'role')
        select_object = Select(select_element)
        select_object.select_by_value('manager')
        first_selected_option = select_object.first_selected_option
        return first_selected_option

    def select_pending_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "pendingButton")
        return element

    def select_pending_plus_button(self):
        element: WebElement = self.driver.find_element(By.CSS_SELECTOR, '[data-id="19"]')
        return element

    def select_pending_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "exampleModal")
        return element

    def select_date(self):
        element: WebElement = self.driver.find_element(By.ID, "validationCustom01")
        return element

    def select_status_from_dropdown(self):
        select_element = self.driver.find_element(By.ID, 'validationCustom02')
        select_object = Select(select_element)
        select_object.select_by_value('approved')
        first_selected_option = select_object.first_selected_option
        return first_selected_option

    def select_reason_input(self):
        element: WebElement = self.driver.find_element(By.ID, "validationCustom03")
        return element

    def select_save_changes_button(self):
        element: WebElement = self.driver.find_element(By.ID, "appDenButton")
        return element

    def select_success_message(self):
        element: WebElement = self.driver.find_element(By.ID, "successMessage")
        return element.text

    def select_failure_message(self):
        element: WebElement = self.driver.find_element(By.ID, "failureMessage")
        return element.text


