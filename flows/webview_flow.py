from pages.home_page import HomePage
from pages.web_view_page import WebViewPage


class WebViewPageFlow:
    def __init__(self, driver):
        self.driver = driver
        self.home = HomePage(driver)
        self.web = WebViewPage(driver)

    def navigate_and_verify_url(self, url, expected_text):
        self.home.open_webview_demo()
        self.web.type_url(url)
        self.web.tap_go()
        actual_title = self.web.get_site_title()
        assert actual_title in expected_text

        # simulate real user behavior
        self.driver.background_app(2)

    def clear_and_verify_value(self,expected_text):
        self.web.clear_input_value()
        actual_text = self.web.get_inputValue()
        assert actual_text in expected_text

   