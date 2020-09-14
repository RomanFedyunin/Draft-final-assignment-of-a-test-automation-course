from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import random
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_current_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_current_login_url(self):
        assert "login" in str(self.browser.current_url), "Login link is not current"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email = str(time.time()) + "@fakemail.org"
        password = 'ASgfahsdbger' + str(random.randint(1, 100))
        email_fields = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_fields.send_keys(email)
        password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1_field.send_keys(password)
        password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2_field.send_keys(password)
        button_registered = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATED)
        button_registered.click()
