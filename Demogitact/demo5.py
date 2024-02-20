
from selenium import webdriver
from selenium.webdriver.edge.service import Service


service = Service(executable_path="edgedriver_win64/msedgedriver.exe")
# options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service)


# service_obj = Service("C:/Users/SRAJEND1/PycharmProjects/Demogitact/edgedriver_win64/msedgedriver.exe")
# driver = webdriver.Edge(Service=service_obj)
driver.get("https://google.com")

