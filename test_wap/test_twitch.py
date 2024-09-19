import time

import pytest
from pytest_assume.plugin import assume
from selenium.common import TimeoutException

from locators import lc_google
from locators import lc_twitch
from page.google import Google
from page.twitch import Twitch


class TestTwitch:

    @pytest.fixture(autouse=True)
    def component(self, init_driver):
        """
        Get the component's object for better readability/usage,
        """
        global google
        global twitch

        google = Google(init_driver)
        twitch = Twitch(init_driver)

    def test_twitch(self, init_driver):
        # Check if it's the first time open Chrome
        google.search_page_or_not()
        if google.wait_and_get_element(lc_google.LANDING_PAGE):
            google.click_element(lc_google.GOT_IT_NO_THANKS_BTN)

        """
        Step1: Go to Twitch
        """
        # Search Twitch
        twitch_url = 'https://m.twitch.tv/'
        google.search(twitch_url)

        """
        Step2: Click in the search icon
        """
        # Check Twitch icon is displayed
        twitch.wait_and_get_element(lc_twitch.TWITCH_ICON)
        with assume:
            assert 'm.twitch.tv' in twitch.get_element_text(
                lc_twitch.TWITCH_URL), f'Current url is {twitch.get_element_text(lc_twitch.TWITCH_URL)}'
        twitch.click_element(lc_twitch.T_SEARCH_ICON)

        """
        Step3: Input StarCraft II
        """
        stream_name = 'StarCraft II'
        # Wait for the search bar showed up
        time.sleep(3)
        # twitch.wait_and_get_element(lc_twitch.T_SEARCH_BAR)
        twitch.search(stream_name)
        # Check the result displayed
        twitch.wait_and_get_element(lc_twitch.RESULT_TITLE)
        with assume:
            assert twitch.get_element_text(
                lc_twitch.RESULT_TITLE) == stream_name, f'Stream name is {twitch.get_element_text(lc_twitch.RESULT_TITLE)}'

        """
        Step4: Scroll down 2 times
        """
        twitch.scroll_screen()
        # print('scroll success1')
        twitch.scroll_screen()
        # print('scroll success2')

        """
        Step5: Select one streamer
        """
        twitch.click_element(lc_twitch.CLICK_VIDEO)

        """
        Step6: On the streamer page wait until all is load and take a screenshot
        """
        init_driver.implicitly_wait(5)
        try:
            twitch.wait_and_get_element(lc_twitch.CHAT_ROOM, timeout=30)
        except TimeoutException:  # Warning popup showed up
            try:
                twitch.wait_and_get_element(lc_twitch.WARNING_POPUP)
                twitch.click_element(lc_twitch.START_WATCHING_BTN)
            except TimeoutException:  # Something wrong page happened
                twitch.wait_and_get_element(lc_twitch.STH_WRONG_PAGE)
                twitch.click_browse_games()
                # Search again
                twitch.search_again(stream_name)
                twitch.wait_and_get_element(lc_twitch.CHAT_ROOM, timeout=30)

        twitch.screenshot()
