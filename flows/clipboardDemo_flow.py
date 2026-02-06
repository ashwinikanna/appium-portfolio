from pages.home_page import HomePage
from pages.clipboardDemo_page import ClipboardDemoPage


class ClipboardDemoFlow:
    def __init__(self, driver):
        self.driver = driver
        self.home = HomePage(driver)
        self.clipboard = ClipboardDemoPage(driver)

    def save_and_verify(self, message):
        self.home.open_clipboard_demo()
        self.clipboard.type_message(message)
        self.clipboard.tap_set_clipboard()
        self.clipboard.tap_refresh()

        # simulate real user behavior
        self.driver.background_app(2)

        saved_text = self.clipboard.get_clipboard_text()
        assert message in saved_text
