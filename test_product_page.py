import pytest
from faker import Faker
from faker import providers

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

old_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
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


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, old_link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, old_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, old_link)
    page.open()
    page.add_to_cart()
    page.should_disappear_success_message()


@pytest.mark.login
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty()
    basket_page.should_be_message_that_basket_is_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        fake = Faker('en-US')
        femail = fake.ascii_free_email()
        fpassword = fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True)
        page.open()
        page.register_new_user(femail, fpassword)
        page.should_be_authorized_user()

    def test_users_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
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
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
