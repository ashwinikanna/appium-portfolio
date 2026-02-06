from .base_page import BasePage


class ClipboardDemoPage(BasePage):
    MESSAGE_INPUT = "messageInput"
    SET_CLIPBOARD_BTN = "setClipboardText"
    CLIPBOARD_TEXT = "clipboardText"
    REFRESH = "refreshClipboardText"
  
    
 
    

    def type_message(self, message):
        el = self.wait_a11y(self.MESSAGE_INPUT)
        el.clear()
        el.send_keys(message)
    
    def tap_set_clipboard(self):
        self.tap_a11y(self.SET_CLIPBOARD_BTN)

    def tap_refresh(self):
        self.tap_a11y(self.REFRESH)

    def get_clipboard_text(self):
        if self.is_android():
         return self.get_text_by_android_resource_id(self.CLIPBOARD_TEXT)
        else:
         return self.get_label_a11y(self.CLIPBOARD_TEXT)
    
