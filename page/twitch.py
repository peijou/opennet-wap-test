from page.base_page import BasePage
from appium import webdriver
from locators import lc_twitch as loc
from appium.options.android import UiAutomator2Options


class Twitch(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def search(self, text: str):
        # self.driver.implicitly_wait(5)
        self.set_text_field(element=loc.T_SEARCH_BAR, text=text)
        self.click_element(loc.T_CLICK_RESULT)

    def click_browse_games(self):
        self.click_element(loc.BROWSE_GAMES_BTN)

    def search_again(self, stream_name):
        self.wait_and_get_element(loc.T_SEARCH_BAR)
        self.search(stream_name)
        # Check the result displayed
        self.wait_and_get_element(loc.RESULT_TITLE)
        self.click_element(loc.CLICK_VIDEO)
        self.wait_and_get_element(loc.CHAT_ROOM, timeout=30)
