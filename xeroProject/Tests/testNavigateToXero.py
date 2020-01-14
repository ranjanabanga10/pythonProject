from selenium import webdriver
import unittest
#import HtmlTestRunner
import time
from xeroProject.Pages.LoginPage import LoginPage
from xeroProject.Pages.HomePage import HomePage


class LoginTest(unittest.TestCase):
    baseURL = "https://login.xero.com/"
    userName = "rbanga@live.com"
    password = "Qatesting2019"
    driver = webdriver.Chrome(
        executable_path = "/Users/ranjanabanga/PycharmProjects/pythonProject/xeroProject/Driver/chromedriver")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_A_login_valid(self):
        login = LoginPage(self.driver)
        login.enter_username(self.userName)
        login.enter_password(self.password)
        login.click_login()
        time.sleep(5)

        homepage = HomePage(self.driver)
        homepage.profile_logo_class
        homepage.logout_linkText

    def test_login_B_incorrect_password(self):
        login = LoginPage(self.driver)
        login.enter_username(self.userName)
        login.enter_incorrect_password("123")
        login.click_login()

        message = self.driver.find_element_by_link_text('Your email or password is incorrect').text
        self.assertEqual("Your email or password is incorrect ", message, 'message not found')
        login.check_invalid_password_message()

    def test_login_C_incorrect_username(self):
        login = LoginPage(self.driver)
        login.enter_username("abc")
        login.enter_incorrect_password(self.password)
        login.click_login()
        message = self.driver.find_element_by_link_text('Your email or password is incorrect').text
        self.assertEqual("Your email or password is incorrect ", message, 'message not found')

    def test_login_D_ForgotPassword(self):
        login = LoginPage(self.driver)
        login.userName_forgotPassword_id(self.userName)
        login.sendLink_button_xpath



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMlTestRunner(output='/Users/ranjanabanga/PycharmProjects/pythonProject'
    #                                                              '/xeroProject/Reports'))
