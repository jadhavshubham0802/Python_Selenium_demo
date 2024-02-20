import time

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass
from pageObject.CheckoutPage import CheckOutPage
from pageObject.HomePage import HomePage
from pageObject.ConfirmPage import ConfirmPage

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()
                log.info(cardText)
                time.sleep(2)

        CheckOutPage.checkOutItems(self).click()

        #time.sleep(5)

        confirmPage = CheckOutPage.finalcheckOutItems(self)

        #time.sleep(5)
        log.info("Entering country name as ind")

        confirmPage.Country().send_keys("ind")

        self.verifyLinkPresence("India")
        #time.sleep(5)

        confirmPage.SelectCountry().click()

        #time.sleep(2)

        confirmPage.MarkCheck().click()

        #time.sleep(5)

        confirmPage.Submitbutton().click()

        #time.sleep(5)

        verifytext = confirmPage.SuccessMessage().text

        assert ("Success! Thank you!" in verifytext)

