from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATED = (By.NAME, 'registration_submit')


class ProductPageLocators:
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".price_color")
    COAST_OF_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    NAME_OF_PRODUCT_BASKET = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    ALERT_INNER_PRODUCT = (By.CSS_SELECTOR, ".alertinner")


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY = (By.XPATH, "//*[@id='content_inner']/p")
