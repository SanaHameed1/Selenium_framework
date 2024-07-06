from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
import time
import pytest


#Accessing Chrome through selenium.....................................................


@pytest.fixture(scope='class')
def chrome_initialization(request):
    service_obj = Service("C:\\Users\\HP\\Selenium framework\\chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(40)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    yield
    driver.close()
