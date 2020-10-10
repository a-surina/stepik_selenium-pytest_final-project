import pytest
from faker import Faker

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

link_coders = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_stars = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
link_registration = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link_coders)
    page.open()
    page.add_to_cart()
    page.should_be_basket_total()
    page.check_basket_total()
    page.should_be_success_message()
    page.check_product_name_in_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_coders)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_coders)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_coders)
    page.open()
    page.add_to_cart()
    page.should_disappear_success_message()


@pytest.mark.login
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link_stars)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link_stars)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_stars)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty()
    basket_page.should_be_message_that_basket_is_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link_registration)
        fake = Faker('en-US')
        femail = fake.ascii_free_email()
        fpassword = fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True)
        page.open()
        page.register_new_user(femail, fpassword)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_users_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_coders)
        page.open()
        page.add_to_cart()
        page.should_be_basket_total()
        page.should_be_success_message()
        expected_price = page.get_product_price()
        actual_price = page.get_basket_total()
        expected_product_name = page.get_product_name()
        actual_product_name = page.get_product_name_in_success_message()
        assert expected_product_name == actual_product_name, \
            f'Expected name "{expected_product_name}", but got "{actual_product_name}"'
        assert expected_price == actual_price, \
            f'Expected price "{expected_price}", but got "{actual_price}"'

    def test_users_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_coders)
        page.open()
        page.should_not_be_success_message()
