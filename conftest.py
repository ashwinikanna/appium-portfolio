
import sys
from pathlib import Path

import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

BUNDLE_ID = "com.appiumpro.the_app"


@pytest.fixture
def driver():
    opts = XCUITestOptions()
    opts.platform_name = "iOS"
    opts.automation_name = "XCUITest"
    opts.device_name = "iPhone 17 Pro"
    opts.platform_version = "26.2"

    # Launch installed app by bundle id
    opts.bundle_id = BUNDLE_ID

    # Keep app data between sessions
    opts.no_reset = True
    opts.full_reset = False
    opts.new_command_timeout = 120

    d = webdriver.Remote("http://127.0.0.1:4723", options=opts)
    yield d
    d.quit()
