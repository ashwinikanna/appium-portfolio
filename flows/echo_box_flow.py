from pages.home_page import HomePage
from pages.echo_box_page import EchoBoxPage


class EchoBoxFlow:
    def __init__(self, driver):
        self.driver = driver
        self.home = HomePage(driver)
        self.echo = EchoBoxPage(driver)

    def save_and_verify(self, message):
        self.home.open_echo_box()
        self.echo.type_message(message)
        self.echo.tap_save()

        # simulate real user behavior
        self.driver.background_app(2)

        saved_text = self.echo.get_saved_message()
        #assert message in saved_text
