
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options



@pytest.fixture
def driver():
    opts = UiAutomator2Options()
    opts.platform_name = "Android"
    opts.automation_name = "UiAutomator2"
    opts.device_name = "Android Emulator"
    opts.udid = "emulator-5554"

    # Since it's already installed, use package/activity:
    opts.app_package = "com.appiumpro.the_app"
    opts.app_activity = "com.appiumpro.the_app.MainActivity"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=opts)
    yield driver
    driver.quit()
