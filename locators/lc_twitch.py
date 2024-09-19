from appium.webdriver.common.appiumby import AppiumBy


# Twitch homepage
TWITCH_URL = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.android.chrome:id/url_bar"]')
TWITCH_ICON = (AppiumBy.XPATH, '//android.view.View[@content-desc="Go to the Twitch home page"]')

# Search page
T_SEARCH_ICON = (AppiumBy.XPATH, '//android.view.View[@content-desc="Search"]/android.widget.TextView')
T_SEARCH_BAR = (AppiumBy.XPATH, '//android.view.View[@resource-id="page-main-content-wrapper"]/android.view.View/android.view.View[2]/android.widget.EditText' or '//android.view.View[@resource-id="page-main-content-wrapper"]/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText')

# Search result page
T_CLICK_RESULT = (AppiumBy.XPATH, '(//android.widget.TextView[@text="StarCraft II"])[1]')
RESULT_TITLE = (AppiumBy.XPATH, '(//android.widget.TextView[@text="StarCraft II"])[1]')

# Stream page
CLICK_VIDEO = (AppiumBy.XPATH, '//android.widget.ListView/android.view.View[2]')
CHAT_ROOM = (AppiumBy.XPATH, '//android.widget.TextView[@text="Welcome to the chat room!"]')
STH_WRONG_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Something went wrong..."]')
BROWSE_GAMES_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="Browse games"]')
START_WATCHING_BTN = (AppiumBy.XPATH, '//android.widget.Button[@text="Start Watching"]')
WARNING_POPUP = (AppiumBy.XPATH, '//android.widget.TextView[@text="Manage the types of content that you see in your content preference "]')