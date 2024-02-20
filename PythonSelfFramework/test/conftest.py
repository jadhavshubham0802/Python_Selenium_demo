import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
import time
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    #browser_name=request.config.getoption("browser_name")
    #if browser_name == "chrome":
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(20)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver   #it is returning driver to that class
    yield
    driver.close()


