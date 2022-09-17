import pytest

from utilities import read_properties
from workflows import web_flows

email = read_properties.get_web_data("email")
password = read_properties.get_web_data("password")


@pytest.fixture
def login_before(pages, wait):
    web_flows.login(pages, wait, email, password)
