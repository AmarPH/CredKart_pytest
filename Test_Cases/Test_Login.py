# We call it as a "Code/Time Optimization" where we use "conftest" file
# to define the piece of code which is going to repeat in actual file
# Eg: Test_Login.py file

import time

import pytest
from selenium.webdriver.common.by import By

from pageObject import LoginPage
from pageObject.LoginPage import Login


class Test_CredKart_Login:

    # def test_title(self, setup):
    #     self.driver = setup
    #     if self.driver.title == "CredKart":
    #         self.driver.save_screenshot(".\\Screen_Shots\\test_title_pass.PNG")
    #         self.driver.close()
    #         assert True
    #     else:
    #         self.driver.save_screenshot(".\\Screen_Shots\\test_title_fail.PNG")
    #         self.driver.close()
    #         assert False
    def test_Login(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)

        self.driver.get("https://automation.credence.in/login")
        # self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()

        self.lp.Textbook_Email("CredenceJune_27@gmail.com")
        # self.driver.find_element(By.ID, "email").send_keys("CredenceJune_27@gmail.com")

        self.lp.Textbook_Password("CredenceJun_27")
        # self.driver.find_element(By.ID, "password").send_keys("CredenceJun_27")

        self.lp.Login_Button()
        print(self.lp.Login_Status())
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        if self.lp.Login_Status() == True:
            self.driver.save_screenshot(".\\Screen_Shots\\test_Login_POM_pass.PNG")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screen_Shots\\test_Login_POM_fail.PNG")
            self.driver.close()
            assert False


        # try:
        #     self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
        #     print("Login Passed")
        #     self.driver.save_screenshot(".\\Screen_Shots\\test_Login_pass.PNG")
        #     self.driver.close()
        #     assert True
        # except:
        #     print("Login Failed")
        #     self.driver.save_screenshot(".\\Screen_Shots\\test_Login_fail.PNG")
        #     self.driver.close()
        #     assert False
