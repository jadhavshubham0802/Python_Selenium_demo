import time
from logging import getLogger

import pytest

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])

        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"]) #used utility for dropdown
        time.sleep(5)
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text
        log.info(alertText)
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param


