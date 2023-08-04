

import time

import pytest
from selenium.webdriver.common.by import By

from Utilities import XLutilis
from pageObject import LoginPage
from pageObject.LoginPage import Login


class Test_CredKart_Login_DDT:
    XLPath = "D:\\Credence Lect Videos\\Python\\Pytest\\CredKart_Pytest_Project\\Test_Cases\\TestData\\LoginTest.xlsx"

    def test_Login_001_DDT(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)

        self.row = XLutilis.RowCount(self.XLPath, "Sheet1")
        print("Row Count ---->:" + str(self.row))
        Login_status_List = []

        for i in range(2, self.row + 1):
            self.email = XLutilis.ReadData(self.XLPath, "Sheet1", i, 2)
            self.password = XLutilis.ReadData(self.XLPath, "Sheet1", i, 3)
            self.exp_result = XLutilis.ReadData(self.XLPath, "Sheet1", i, 4)

            self.lp.Click_Login_link()
            self.lp.Textbook_Email(self.email)
            self.lp.Textbook_Password(self.password)
            self.lp.Login_Button()
            # print(self.lp.Login_Status())

            if self.lp.Login_Status() == True:

                if self.exp_result == "Pass":
                    Login_status_List.append("Pass")
                    self.driver.save_screenshot(".\\Screen_Shots\\test_Login_001_DDT.PNG")
                    self.lp.Menu_Button()
                    self.lp.Click_Logout()
                    XLutilis.WriteData(self.XLPath, "Sheet1", i, 5, "Pass")

                elif self.exp_result == "Fail":
                    Login_status_List.append("Pass")
                    self.driver.save_screenshot(".\\Screen_Shots\\test_Login_001_DDT.PNG")
                    self.lp.Click_Menu_Xpath()
                    self.lp.click_Logout_Xpath()
                    XLutilis.WriteData(self.XLPath, "Sheet1", i, 5, "Fail")

            if self.lp.Login_Status() == False:
                if self.exp_result == "Pass":
                    Login_status_List.append("Pass")
                    self.driver.save_screenshot(".\\Screen_Shots\\test_Login_001_DDT.PNG")
                    XLutilis.WriteData(self.XLPath, "Sheet1", i, 5, "Fail")

                elif self.exp_result == "Fail":
                    Login_status_List.append("Pass")
                    self.driver.save_screenshot(".\\Screen_Shots\\test_Login_001_DDT.PNG")
                    XLutilis.WriteData(self.XLPath, "Sheet1", i, 5, "Pass")

        print(Login_status_List)
        if "Fail" not in Login_status_List:
            assert True
        else:
            assert False