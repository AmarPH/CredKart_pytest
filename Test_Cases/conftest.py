
# We call it as a "Code/Time Optimization" where we use "conftest" file
# to define the piece of code which is going to repeat in actual file
# Eg: Test_Login.py file

import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.credence.in/")
    return driver

def pytest_metadata(metadata):
    # This commands to Add/Customize things in HTML report

    metadata["Class"] = "Credence"
    metadata["Batch"] = "CT14"
    metadata["URL"] = "https://automation.credence.in/"

    # This commands to Remove/Customize things in HTML report
    metadata.pop("Platform", None)


@pytest.fixture(params=[
    ("CredenceJune_27@gmail.com","CredenceJun_27"),
    ("CredenceJuen_27@gmail.com","CredenceJun_27"),
    ("CredenceJune_27@gmail.com","CredenceJun_0027"),
    ("CredenceJun_27@gmail.com","CredenceJuen_0027")
])
def getDataforLogin(request):
    return request.param