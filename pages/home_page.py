from .base_page import BasePage


class HomePage(BasePage):
    ECHO_BOX_MENU = "Echo Box Write something and save to local memory"
    ECHO_BOX_ANDROID = "RNE__LISTITEM__padView"
    CLIPBOARD_DEMO_MENU = "Clipboard Demo Mess around with the clipboard"
    WEBVIEW_DEMO_MENU = "Webview Demo Explore the possibilities of hybrid apps"
    WEBVIEW_DEMO_MENU_ANDROID = "(//android.view.ViewGroup[@resource-id='RNE__LISTITEM__padView'])[4]"
    CLIPBOARD_DEMO_ANDROID = "(//android.view.ViewGroup[@resource-id='RNE__LISTITEM__padView'])[3]"





    def open_echo_box(self):
        if self.is_android():
            self.tap_by_android_resource_id(self.ECHO_BOX_ANDROID)
        else:
            self.tap_a11y(self.ECHO_BOX_MENU)

    def open_clipboard_demo(self):
        if self.is_android():
            self.tap_xpath(self.CLIPBOARD_DEMO_ANDROID)
        else:
            self.tap_a11y(self.CLIPBOARD_DEMO_MENU)

    def open_webview_demo(self):
        if self.is_android():
            self.tap_xpath(self.WEBVIEW_DEMO_MENU_ANDROID)
        else:
            self.tap_a11y(self.WEBVIEW_DEMO_MENU)
