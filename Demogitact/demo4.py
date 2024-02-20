from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

# Specify the full path to msedgedriver.exe
edge_driver_path = r"C:\Users\SRAJEND1\PycharmProjects\Demogitact\edgedriver_win64\msedgedriver.exe"

# Create EdgeOptions instance
edge_options = EdgeOptions()
# Set the path to the Edge WebDriver executable
edge_options.binary_location = edge_driver_path

# Initialize Edge WebDriver with EdgeService and EdgeOptions
service_obj = EdgeService(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service_obj, options=edge_options)
driver.get("https://google.com")
