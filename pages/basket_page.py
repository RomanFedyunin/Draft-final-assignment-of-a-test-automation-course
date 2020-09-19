from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_bascket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEM), "В корзине есть товар, который мы не добавляли"

    def check_basket_is_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEM), 'В корзине есть товар, который мы не добавляли'

    def should_be_text_empty_basket(self):
        element = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY)
        assert "Your basket is empty" in element.text, 'Нет текста о том, что корзина пуста'
