from flows.clipboardDemo_flow import ClipboardDemoFlow


def test_clipboard_demo_persistence(driver):
    ClipboardDemoFlow(driver).save_and_verify("Hello Appium")