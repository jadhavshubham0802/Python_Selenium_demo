from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryName = (By.ID, "country")
    selectCountry1 = (By.LINK_TEXT, "India")
    markcheck1 = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    message1 = (By.CSS_SELECTOR, "[class*='alert-success']")

    def Country(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def SelectCountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry1)


    def MarkCheck(self):
        return self.driver.find_element(*ConfirmPage.markcheck1)

    def Submitbutton(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def SuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.message1)

