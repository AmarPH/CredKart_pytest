

import time
from selenium.webdriver.common.by import By


class Test_CredKart_Login_Params:

    def test_login_params(self, setup, getDataforLogin):
        self.driver = setup
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        self.driver.find_element(By.ID, "email").send_keys(getDataforLogin[0])
        self.driver.find_element(By.ID, "password").send_keys(getDataforLogin[1])
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

