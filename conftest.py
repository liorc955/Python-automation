import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
import time

from page_objects.nopcommerce.CreateCustomerPage import CreateCustomer
from page_objects.nopcommerce.CustomersPage import Customers
from page_objects.nopcommerce.LoginPage import Login
from page_objects.nopcommerce.MegaMenuPage import MegaMenu
from utilities import custom_logger, read_properties
from selenium.webdriver.support.ui import WebDriverWait
from utilities.Base import Base


# Before Module
@pytest.fixture(scope="module", autouse=True)
def setup(get_param):
    custom_logger.loggen()
    platform = get_param["platform"]
    browser = get_param["browser"]
    if platform == "web":
        if browser == "chrome":
            Base.DRIVER = initChromeDriver()
        elif browser == "firefox":
            Base.DRIVER = initFireFoxDriver()
        else:
            raise ValueError("Please check again the browser (chrome and firefox only)")
        Base.DRIVER.maximize_window()
        Base.DRIVER.implicitly_wait(4)
        Base.WAIT = WebDriverWait(Base.DRIVER, 10)
        init_pages()
    elif platform != 'api':
        raise ValueError("Please check again the platform (api and web only)")

    yield  # After Module
    if platform == 'web':
        Base.DRIVER.quit()


def init_pages():
    Base.LOGIN_PAGE = Login(Base.DRIVER)
    Base.MEGA_MENU = MegaMenu(Base.DRIVER)
    Base.CUSTOMER = Customers(Base.DRIVER)
    Base.CREATE_CUSTOMER = CreateCustomer(Base.DRIVER)


def initChromeDriver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def initFireFoxDriver():
    return webdriver.Firefox(service=Service(GeckoDriverManager().install()))


# Before Method
@pytest.fixture(scope="function", autouse=True)
def before(request, get_param):
    if get_param["platform"] == "web":
        Base.DRIVER.get(read_properties.get_web_data("baseUrl"))


# set up a hook to be able to check the status test
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


# check if a test has failed or passed
@pytest.fixture(scope="function", autouse=True)
def test_status_check(request, get_param):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    logger = custom_logger.loggen()
    if request.node.rep_setup.failed:
        logger.info(
            f"******************{str(request.node.nodeid)} Setting Failed******************"
        )
    elif request.node.rep_setup.passed:
        logger.info(
            f"******************{str(request.node.nodeid)} Setting Passed******************"
        )
        if request.node.rep_call.failed:
            if get_param["platform"] == "web":
                take_screenshot(request.node.nodeid)
            logger.info(
                f"******************{str(request.node.nodeid)} Executing Failed******************"
            )
        elif request.node.rep_call.passed:
            logger.info(
                f"******************{str(request.node.nodeid)} Executing Passed******************"
            )


# make a screenshot with the name of the test
def take_screenshot(nodeid):
    time.sleep(2)
    file_name = (
            ".\\Screenshots\\fail_" + nodeid.replace("/", "_").replace("::", "__") + ".png"
    )
    allure.attach(
        Base.DRIVER.get_screenshot_as_png(),
        name=file_name,
        attachment_type=AttachmentType.PNG,
    )


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--platform")


@pytest.fixture(scope="module", autouse=True)
def get_param(request):
    config_param = {
        "browser": request.config.getoption("--browser"),
        "platform": request.config.getoption("--platform"),
    }
    return config_param