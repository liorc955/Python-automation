import pytest

from utilities import readProperties
from workflows import webFlows

email = readProperties.get_web_data("email")
password = readProperties.get_web_data("password")


@pytest.fixture
def login_before(pages, wait):
    webFlows.login(pages, wait, email, password)
