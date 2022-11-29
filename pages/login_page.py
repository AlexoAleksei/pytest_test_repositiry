from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find("login"), "Login is not presented in a current url!"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert LoginPageLocators.LOGIN_FORM, "Login Form is not presented on a login page!"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert LoginPageLocators.REGISTER_FORM, "Registrarion Form is not presented on a login page!"