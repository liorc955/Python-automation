import pytest

from utilities.readProperties import ReadConfig
from workflows.WebFlows import WebFlows

email = ReadConfig.get_web_data("email")
password = ReadConfig.get_web_data("password")


@pytest.fixture
def login_before(pages, wait):
    WebFlows.login(pages, wait, email, password)
