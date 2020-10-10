from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
