"""
BasePage object class and generic methods only
"""
import os
import pprint
import sys

from selenium.common import TimeoutException, NoSuchElementException, ElementNotVisibleException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    BasePage class to contain commonly used page interactions to avoid code repeatability
    and follow DRY principle
    """

    # BASE PAGE CONSTRUCTOR

    def __init__(self, driver: WebDriver, url=None, title=None, pybug=None):
        """
        Main constructor for all page objects, with attributes common to any page

        :param driver: WebDriver instance used by the page instance
        :param url: URL of the page
        :param title: Page Title
        :param pybug: Logger for the page object
        """
        self.driver = driver
        self.url = url
        self.title = title
        if pybug:
            self.pybug = pybug
        else:
            self.pybug = pprint.pprint
        self.action = ActionChains(self.driver)

    @staticmethod
    def get_exception():
        """
            Method to return sys.exc_info() exceptions
        """
        return sys.exc_info()

    @staticmethod
    def meta_raise(exc_info):
        """
            Method to raise caught exceptions with traceback
        """
        raise exc_info[0](exc_info[1]).with_traceback(exc_info[2])

    def wait_and_get_element(self, element: tuple[str,str], timeout: float = 20) -> WebElement:
        """
        Method to deal with waiting for an element and finding it in the DOM.

        :param element: WebElement's locator as a `tuple`
        :param timeout: Time in seconds we want to wait when locating elements
        :return: WebElement to be interacted with
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.all_of(
                 EC.visibility_of_element_located(element),
                    EC.presence_of_element_located(element),
                )
            )
            return self.driver.find_element(*element)
        except (TimeoutException, NoSuchElementException,
                ElementNotVisibleException):
            error = self.get_exception()
            self.meta_raise(error)

    def click_element(self, element: tuple[str,str] | WebElement, timeout: float = 10) -> None:
        """
        Method to click() a WebElement

        :param element: WebElement's locator as a `tuple`
        :param timeout: Amount of time to pass to `wait_and_get_element`
        """
        try:
            if isinstance(element, tuple):
                self.wait_and_get_element(element, timeout).click()
            else:
                element.click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            if isinstance(element, tuple):
                element = self.wait_and_get_element(element, timeout)
            self.action.click(element).perform()

    def clear_text_field(self, element: tuple[str,str], timeout: float = 10) -> None:
        """
        Method to clear() a WebElement's text

        :param element: WebElement's locator as a `tuple`
        :param timeout: Amount of time to pass to `wait_and_get_element`
        """
        self.wait_and_get_element(element, timeout).clear()

    def set_text_field(self, element: tuple[str,str], text, timeout: float = 10) -> None:
        """
        Method to send_keys() to a WebElement

        :param element: WebElement's locator as a `tuple`
        :param timeout: Amount of time to pass to `wait_and_get_element`
        :param text: Input text
        """
        self.clear_text_field(element, timeout)
        self.driver.find_element(*element).send_keys(text)

    def get_element_text(self, element: tuple[str,str] | WebElement, timeout: float = 10) -> str:
        """
        Method to get text from a WebElement

        :param element: WebElement's locator as a `tuple`
        :param timeout: Amount of time to pass to `wait_and_get_element`
        :return: Text of WebElement
        """
        return self.wait_and_get_element(element, timeout).text

    def scroll_screen(self, direction: str = 'down'):
        """
        This gesture performs scroll gesture on the given element/area

        :param direction: string, up, down, left and right
        """
        self.driver.execute_script('mobile: scrollGesture', {
            'left': 100, 'top': 100, 'width': 200, 'height': 200,
            'direction': direction,
            'percent': 10.0
        })

    def screenshot(self, file_name: str = 'screenshot.png'):
        directory = '%s/' % os.getcwd()
        self.driver.save_screenshot(directory + file_name)

