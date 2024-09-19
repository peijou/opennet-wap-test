from appium.webdriver.common.appiumby import AppiumBy


# First time enter the Chrome
WELCOME2CHROME = (AppiumBy.XPATH, '//*[@text="Welcome to Chrome"]' or '//android.widget.TextView[@resource-id="com.android.chrome:id/title"]')
WITHOUT_LOGIN_BTN = (AppiumBy.XPATH, '//*[@text="Use without an account"]' or '//android.widget.Button[@resource-id="com.android.chrome:id/signin_fre_dismiss_button"]')
LANDING_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Enhanced ad privacy in Chrome"]' or '//android.widget.TextView[@text="Chrome notifications make things easier"]')
GOT_IT_NO_THANKS_BTN = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.chrome:id/ack_button"]' or '//*[@text="No thanks"]')
# Surfing the Internet
SEARCH_BAR = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]' or '//*[@text="Search or type web address"]')
CLICK_RESULT = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.android.chrome:id/line_1"]')