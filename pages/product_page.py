from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        global price_of_product
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        global name_of_product
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        button_add_to_basket.click()

    def check_product_add_to_basket(self):
        name_product_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_BASKET).text
        assert name_of_product == name_product_basket, "Название товара не совпадает"

    def check_coast_basket(self):
        coast = self.browser.find_element(*ProductPageLocators.COAST_OF_BASKET).text
        assert price_of_product == coast, "Неверная стоимость!"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_alert_add_product(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ALERT_INNER_PRODUCT), "Есть сообщение о добавлении товара"

    def should_be_not_alert_add_product(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_INNER_PRODUCT), \
            "Товар не добавлен, но есть алерт об усешном добавлении "

    def should_be_alert_product_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.ALERT_INNER_PRODUCT), "Алерт о добавлении товара не исчезает"
