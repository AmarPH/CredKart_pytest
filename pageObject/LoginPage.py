import time

from selenium.webdriver.common.by import By


class Login:
    Textbook_Email_Xpath = (By.XPATH, "//input[@id='email']")
    Textbook_Password_Xpath = (By.XPATH, "//input[@id='password']")
    Login_Button_Xpath = (By.XPATH, "//button[@type='submit']")
    Login_Status_Xpath = (By.XPATH, "//h2[normalize-space()='CredKart']")
    Click_Menu_Xpath = (By.XPATH, "//a[@role='button']")
    click_Logout_Xpath = (By.XPATH, "//a[normalize-space()='Logout']")
    CLick_Login_button = (By.XPATH, "//a[normalize-space()='Login']")

    def __init__(self, driver):
        self.driver = driver

    def login_url(self):
        self.driver.get(*Login.Login_Url)

    def Click_Login_link(self):
        self.driver.find_element(*Login.CLick_Login_button).click()

    def Textbook_Email(self, email):
        self.driver.find_element(*Login.Textbook_Email_Xpath).send_keys(email)

    def Textbook_Password(self, password):
        self.driver.find_element(*Login.Textbook_Password_Xpath).send_keys(password)

    def Login_Button(self):
        self.driver.find_element(*Login.Login_Button_Xpath).click()

    def Menu_Button(self):
        self.driver.find_element(*Login.Click_Menu_Xpath).click()

    def Click_Logout(self):
        self.driver.find_element(*Login.click_Logout_Xpath).click()

    def Login_Status(self):
        try:
            self.driver.find_element(*Login.Login_Status_Xpath)
            print("Test Pass")
            return True
        except:
            print("Test Fail")
            return False
