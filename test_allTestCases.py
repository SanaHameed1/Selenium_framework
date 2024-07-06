from select import select
from selenium import webdriver
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
import time
import pytest
from utilities.Base_class import Base_Class


class MyClass(Base_Class):

    def __init__(self, driver):
        self.driver = driver

    def test_radiobutton(self):

        result = self.driver.find_elements(By.XPATH, "//label/input[@class='radioButton']")
        result[1].click()
        self.driver.get_screenshot_as_file("sana.png")
        time.sleep(2)

    def test_checkbox(self):

        checkboxes = self.driver.find_elements(By.XPATH, "//label/input[@type='checkbox']")
        for checkbox in checkboxes:
            if checkbox.get_attribute("value") == "option2":
                checkbox.click()
                time.sleep(2)

    def test_dropdown(self):

        dropdown = Select(self.driver.find_element(By.ID, "dropdown-class-example"))
        dropdown.select_by_visible_text("Option2")
        time.sleep(2)
