from selenium.common import TimeoutException

from page.base_page import BasePage
from appium import webdriver
from locators import lc_google as loc


class Google(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def search_page_or_not(self):
        try:
            self.wait_and_get_element(loc.WELCOME2CHROME)
            self.click_element(loc.WITHOUT_LOGIN_BTN)
        except TimeoutException:
            pass

    def search(self, text: str):
        self.set_text_field(element=loc.SEARCH_BAR, text=text)
        self.click_element(loc.CLICK_RESULT)
