import time

from selenium.webdriver.common.by import By


class Login:
    Textbook_Email_Xpath = (By.XPATH, "//input[@id='email']")
    Textbook_Password_Xpath = (By.XPATH, "//input[@id='password']")
    Login_Button_Xpath = (By.XPATH, "//button[@type='submit']")
    Login_Status_Xpath = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self, driver):
        self.driver = driver

    def login_url(self):
        self.driver.get(*Login.Login_Url)

    def Textbook_Email(self, email):
        self.driver.find_element(*Login.Textbook_Email_Xpath).send_keys(email)

    def Textbook_Password(self, password):
        self.driver.find_element(*Login.Textbook_Password_Xpath).send_keys(password)

    def Login_Button(self):
        try:
            self.driver.find_element(*Login.Login_Button_Xpath).click()
            print("-------------> Login")
            return True
        except:
            print("Error")
            return False

    def Login_Status(self):
        try:
            self.driver.find_element(*Login.Login_Status_Xpath)
            print("Test Pass")
            return True
        except:
            print("Test Fail")
            return False
