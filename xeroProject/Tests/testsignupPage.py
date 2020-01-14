from selenium import webdriver
from xeroProject.Pages.SignupPage import SignUp
import unittest
class signupTestpage(unittest.TestCase):

    baseURL = "https://www.xero.com/us/"
    driver = webdriver.Chrome(
        executable_path="/Users/ranjanabanga/PycharmProjects/pythonProject/xeroProject/Driver/chromedriver")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_01A_signup_page(self):
        signup = SignUp(self.driver)
        signup.enter_firstName_textbox_Name("Malisha")
        signup.enter_lastName_textbox_Name("Paul")
        signup.enter_emailAddress_textbox_Name("coolgurlrb@aol.com")
        signup.enter_phoneNumber_textbox_Name("2345678989")
        signup.enter_location_textbox_Name("USA")
        signup.click_reCaptcha_Chkbx()
        signup.click_termAccepted_Chkbx()
        signup.click_submit_xpath()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()