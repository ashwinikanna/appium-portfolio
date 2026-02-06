from .base_page import BasePage


class EchoBoxPage(BasePage):
    MESSAGE_INPUT = "messageInput"
    SAVE_BTN = "messageSaveBtn"
    SAVED_MESSAGE = "savedMessage"
    SAVED_MESSAGE_ANDROID = "android.widget.TextView"
    

    def type_message(self, message):
        el = self.wait_a11y(self.MESSAGE_INPUT)
        el.clear()
        el.send_keys(message)

    def tap_save(self):
        self.tap_a11y(self.SAVE_BTN)

    def get_saved_message(self):
        if self.is_android():
          return self.get_text_by_android_resource_id("savedMessage")
        else:
          return self.get_label_a11y(self.SAVED_MESSAGE)
    
