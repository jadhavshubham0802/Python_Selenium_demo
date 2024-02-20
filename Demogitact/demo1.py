from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

# Create EdgeOptions instance
edge_options = EdgeOptions()
# Add any desired Edge options
# edge_options.add_argument('--some-option')
# No need to specify executable_path
service_obj = EdgeService()

# Initialize Edge WebDriver
driver = webdriver.Edge(service=service_obj, options=edge_options)
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
