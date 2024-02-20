from selenium import webdriver

# Specify the full path to msedgedriver.exe
edge_driver_path = r"C:\Users\SRAJEND1\PycharmProjects\Demogitact\edgedriver_win64\msedgedriver.exe"

# Initialize Edge WebDriver
driver = webdriver.Edge(executable_path=edge_driver_path, port=9515)

# Open Google website as an example
driver.get("https://google.com")
