from flows.webview_flow import WebViewPageFlow


def test_webview_persistence(driver):
    WebViewPageFlow(driver).navigate_and_verify_url("https://appiumpro.com",'Your weekly')
    WebViewPageFlow(driver).clear_and_verify_value("https://appiumpro.com")
