import time

from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")              #it is tpuple
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.CSS_SELECTOR, "#navbarResponsive a")
    finalcheckout = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)  #we use * to deserialize it it is mandatory

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        time.sleep(5)
        return self.driver.find_element(*CheckOutPage.checkOut)

    def finalcheckOutItems(self):
        #time.sleep(5)
        self.driver.find_element(*CheckOutPage.finalcheckout).click()
        confirmPage = ConfirmPage(self.driver)
        #time.sleep(5)
        return confirmPage
