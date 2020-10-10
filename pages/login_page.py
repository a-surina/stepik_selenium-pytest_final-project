from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_text = "login"
        assert url_text in self.browser.current_url, \
            f'Text "{url_text}" is missing in current url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is missing"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is missing"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_confirmation_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRMATION_FIELD)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirmation_field.send_keys(password)
        submit_button.click()

