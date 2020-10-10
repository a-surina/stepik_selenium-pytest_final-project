from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_page_header()

    def should_be_page_header(self):
        assert self.is_element_present(*BasketPageLocators.HEADER), \
            "Header is missing"
        header_expected_text = "Basket"
        header_actual_text = self.browser.find_element(*BasketPageLocators.HEADER).text
        assert header_actual_text == header_expected_text, \
            f'Expected page header "{header_expected_text}", but found "{header_expected_text}"'

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), \
            "Basket is not empty"

    def should_not_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT), \
            "Basket is empty"

    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Message that basket is empty not found"
        message_text = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        expected_text = "Your basket is empty."
        assert expected_text in message_text, \
            f'Expected message to include "{expected_text}", but actual message is "{message_text}"'

    def should_not_be_message_that_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Message that basket is empty is present"
