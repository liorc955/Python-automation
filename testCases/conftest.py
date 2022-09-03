import pytest

from utilities import readProperties
from workflows import WebFlows

email = readProperties.get_web_data("email")
password = readProperties.get_web_data("password")


@pytest.fixture
def login_before(pages, wait):
    WebFlows.login(pages, wait, email, password)
