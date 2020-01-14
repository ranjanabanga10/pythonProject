from xeroProject.Locators.locators import Locators

class SignUp():
    def __init__(self, driver):
        self.driver = driver
        self.freeTrial_link_xpath = Locators.free_trial_button_xpath
        self.firstName_textbox_Name = Locators.enter_firstName_Name
        self.lastName_textbox_Name = Locators.enter_lastName_Name
        self.emailAddress_textbox_Name = Locators.enter_emailAddress_Name
        self.phoneNumber_textbox_Name = Locators.enter_phoneNumber_Name
        self.location_Name_textbox_Name = Locators.enter_location_Name
        self.click_reCaptcha_button_id = Locators.click_recaptcha_id
        self.check_termAccepted_Name = Locators.check_termAccepted_Name
        self.click_submit_xpath = Locators.click_submit_xpath

    def click_freeTrial_button(self):
        self.driver.find_element_by_xpath(self.freeTrial_link_xpath).click()

    def enter_firstName_textbox_Name(self, Fname):
        self.driver.find_element_by_name(self.firstName_textbox_Name).send_keys(Fname)

    def enter_lastName_textbox_Name(self, Lname):
        self.driver.find_element_by_name(self.lastName_textbox_Name).send_keys(Lname)

    def enter_emailAddress_textbox_Name(self, email):
        self.driver.find_element_by_name(self.emailAddress_textbox_Name).send_keys(email)

    def enter_phoneNumber_textbox_Name(self, phone):
        self.driver.find_element_by_name(self.phoneNumber_textbox_Name).send_keys(phone)

    def enter_location_textbox_Name(self, location):
        self.driver.find_element_by_name(self.location_Name_textbox_Name).send_keys(location)

    def click_reCaptcha_Chkbx(self):
        self.driver.find_element_by_name(self.click_reCaptcha_button_id)

    def click_termAccepted_Chkbx(self):
        self.driver.find_element_by_name(self.check_termAccepted_Name)

    def click_submit_xpath(self):
        self.driver.find_element_by_name(self.click_submit_xpath())