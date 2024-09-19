from appium.webdriver.common.appiumby import AppiumBy


# First time enter the Chrome
WELCOME2CHROME = (AppiumBy.XPATH, '//*[@text="Welcome to Chrome"]')
WITHOUT_LOGIN_BTN = (AppiumBy.XPATH, '//*[@text="Use without an account"]')
LANDING_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Chrome notifications make things easier"]')
NO_THANKS_BTN = (AppiumBy.XPATH, '//*[@text="No thanks"]')

# Surfing the Internet
SEARCH_BAR = (AppiumBy.XPATH, '//*[@text="Search or type web address"]')
CLICK_RESULT = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.android.chrome:id/line_1"]')