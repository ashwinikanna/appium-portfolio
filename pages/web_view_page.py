from .base_page import BasePage


class WebViewPage(BasePage):
    MESSAGE_INPUT = "XCUIElementTypeTextField"
    MESSAGE_INPUT_ANDROID = "urlInput"
    GO_BTN = "navigateBtn"
    WEBSITE = "Your weekly"
    WEBSITE_ANDROID = "android.widget.TextView"
    CLEAR_BTN = "clearBtn"

    def type_url(self, message):
        if self.is_android():
         el = self.wait_a11y(self.MESSAGE_INPUT_ANDROID)
        else:
         el = self.wait_className(self.MESSAGE_INPUT)
        el.clear()
        el.send_keys(message)

    def tap_go(self):
        self.tap_a11y(self.GO_BTN)

    def get_site_title(self):
        if self.is_android():
         return self.get_text_by_class(self.WEBSITE_ANDROID)
        else:       
         return self.get_label_a11y(self.WEBSITE)
    
    def tap_clear_btn(self):
        self.tap_a11y(self.CLEAR_BTN)

    def clear_input_value(self):
        self.tap_clear_btn()

    def get_inputValue(self):
        if self.is_android():
          return self.get_text_a11y(self.MESSAGE_INPUT_ANDROID)
        else:
          return self.get_value_by_class(self.MESSAGE_INPUT)
       
