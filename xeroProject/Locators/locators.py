class Locators():

    # Login page objects
    username_textbox_name = "userName"
    password_textbox_name = "password"
    login_button_xpath = "//button[@id='submitButton']"
    invalidPassword_message_xpath = "//p[contains(text(),'Your email or password is incorrect')]"
    forgot_password_click_xpath = "//a[@class='forgot-password-advert']"
    username_forgotPassword_id = "UserName"
    click_sendLink_xpath = "//a[@class='x-btn blue']"

    # Home page objects

    profile_logo_class = "//a[@class='username']"
    logout_linkText = "logout"

    # SignUp page objects

    free_trial_button_xpath = "//a[@class='btn btn-primary global-ceiling-bar-btn']"
    enter_firstName_Name = "FirstName"
    enter_lastName_Name = "LastName"
    enter_emailAddress_Name = "EmailAddress"
    enter_phoneNumber_Name = "PhoneNumber"
    enter_location_Name = "LocationCode"
    click_recaptcha_id = "recaptcha-anchor"
    check_termAccepted_Name = "TermsAccepted"
    click_submit_xpath = "//span[@class='g-recaptcha-submit']"
