
# We call it as a "Code/Time Optimization" where we use "conftest" file
# to define the piece of code which is going to repeat in actual file
# Eg: Test_Login.py file

import time

import pytest
from selenium.webdriver.common.by import By


class Test_CredKart_Login:

    def test_title(self, setup):
        self.driver = setup
        if self.driver.title == "CredKart":
            self.driver.save_screenshot(".\\Screen_Shots\\test_title_pass.PNG")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screen_Shots\\test_title_fail.PNG")
            self.driver.close()
            assert False

    @pytest.mark.skip
    def test_Login(self, setup):
        self.driver = setup
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        self.driver.find_element(By.ID, "email").send_keys("CredenceJune_27@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("CredenceJun_27")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(2)

        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login Passed")
            self.driver.save_screenshot(".\\Screen_Shots\\test_Login_pass.PNG")
            self.driver.close()
            assert True
        except:
            print("Login Failed")
            self.driver.save_screenshot(".\\Screen_Shots\\test_Login_fail.PNG")
            self.driver.close()
            assert False

