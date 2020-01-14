from xeroProject.Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.profile_logo_class = Locators.profile_logo_class
        self.logout_linkText = Locators.logout_linkText

    def click_profile_logo(self):
        self.driver.find_element_by_class(self.profile_logo_class).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_linkText).click()