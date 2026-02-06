import time
import os

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver, timeout=12):
        self.driver = driver
        self.timeout = timeout

    def pause(self, seconds: float = 0.5):
    # set SLOWMO=1 to enable
     if os.getenv("SLOWMO") == "1":
        time.sleep(seconds)
    
    def is_android(self) -> bool:
        return (self.driver.capabilities.get("platformName") or "").lower() == "android"

    def wait_a11y(self, acc_id, timeout=None):
        """
        Wait until an element (by Accessibility ID) is visible, then return it.
        """
        wait_time = timeout if timeout is not None else self.timeout

        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, acc_id))
        )
    
    def wait_className(self, className, timeout=None):
        """
        Wait until an element (by Class name) is visible, then return it.
        """
        wait_time = timeout if timeout is not None else self.timeout

        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located((AppiumBy.CLASS_NAME, className))
        )
    

    def tap_a11y(self, acc_id):
        """
        Wait for an element by Accessibility ID and tap it.
        """
        self.wait_a11y(acc_id).click()

    def tap_by_class(self, className):
        """
        Wait for an element by Accessibility ID and tap it.
        """
        self.wait_className(className).click()   

    def get_label_a11y(self, acc_id):
        """
        Read visible text from an element (best for labels/static text).
        """
        el = self.wait_a11y(acc_id)
        return (el.get_attribute("label") or el.text or "").strip()
    
    def get_text_a11y(self, acc_id):
        """
        Read visible text from an element (best for labels/static text).
        """
        el = self.wait_a11y(acc_id)
        return (el.get_attribute("text") or el.text or "").strip()

    def get_value_a11y(self, acc_id):
        """
        Read the 'value' attribute (best for text fields).
        """
        el = self.wait_a11y(acc_id)
        return (el.get_attribute("value") or "").strip()
    

    def get_value_by_class(self, className):
        """
        Read the 'value' attribute (best for text fields).
        """
        el = self.wait_className(className)
        return (el.get_attribute("value") or "").strip()
    
    def get_text_by_class(self, className):
        """
        Read the 'value' attribute (best for text fields).
        """
        el = self.wait_className(className)
        return (el.get_attribute("text") or "").strip()
    
    def tap_echo_box_android(self):
     el = WebDriverWait(self.driver, self.timeout).until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[1]'
        ))
    ) 
     el.click()


    def tap_xpath(self, xpath, timeout=None):
     wait_time = timeout if timeout else self.timeout
     el = WebDriverWait(self.driver, wait_time).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
    )
     el.click()
 

    def get_text_by_android_resource_id(self, rid: str, timeout=None) -> str:
      wait_time = timeout if timeout is not None else self.timeout
      ui = f'new UiSelector().resourceId("{rid}")'   # <-- double quotes guaranteed

      el = WebDriverWait(self.driver, wait_time).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, ui))
    )
      return (el.text or el.get_attribute("text") or "").strip()
    
    def tap_by_android_resource_id(self, rid: str, timeout=None) -> str:
      wait_time = timeout if timeout is not None else self.timeout
      ui = f'new UiSelector().resourceId("{rid}")'   # <-- double quotes guaranteed

      el = WebDriverWait(self.driver, wait_time).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, ui))
    )
      el.click()
      
    