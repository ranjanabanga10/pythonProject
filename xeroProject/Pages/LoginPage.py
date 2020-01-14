from xeroProject.Locators.locators import Locators
class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_xpath = Locators.login_button_xpath
        self.invalidPassword_message_xpath = Locators.invalidPassword_message_xpath
        self.forgot_password_click_xpath = Locators.forgot_password_click_xpath
        self.userName_forgotPassword_id = Locators.username_forgotPassword_id
        self.sendLink_button_xpath = Locators.click_sendLink_xpath

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def enter_incorrect_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def check_invalid_password_message(self, message):
        msg = self.driver.find_element_by_xpath(self.invalidPassword_message_xpath).text

    def click_forgot_password_option(self):
        self.driver.find_element_by_xpath(self.forgot_password_click_xpath).click()

    def enter_userName_forgotPassword(self, username):
        self.driver.find_element_by_id(self.userName_forgotPassword_id).send_keys(username)

    def click_sendLink_button(self):
        self.driver.find_element_by_xpath(self.sendLink_button_xpath).click()
