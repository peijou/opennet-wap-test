import pytest
from appium.options.common import AppiumOptions
from appium import webdriver
from typing import Any, Dict

@pytest.fixture
def init_driver():
    """
    Main fixture for setting up and tearing down the WebDriver for Android emulator
    """
    print(f"\n--------------- Setting up WebDriver  ---------------\n")

    cap: Dict[str, Any] = {
        "platformName": "Android",
        "appium:platformVersion": "14",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UIAutomator2",
        "appPackage": "com.android.chrome",
        "appActivity": "com.google.android.apps.chrome.Main",
        "language": "en",
        "locale": "US"
    }

    url = 'http://localhost:4723'

    # Create the driver instance using the desired capabilities
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

    # Yield the driver instance to use in tests
    yield driver

    print(f"\n--------------- Tearing Down WebDriver ---------------\n")
    driver.quit()