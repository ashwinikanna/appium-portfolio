import pytest
pytestmark = pytest.mark.mobile

from flows.echo_box_flow import EchoBoxFlow


def test_echo_box(driver):
    EchoBoxFlow(driver).save_and_verify("Hello Appium")
    