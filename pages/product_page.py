from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price.text

    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return name.text

    def should_be_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), \
            "Basket total is missing"

    def get_basket_total(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        return basket_total.text

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is missing"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should have disappeared"

    def get_product_name_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE)
        return product_name.text
