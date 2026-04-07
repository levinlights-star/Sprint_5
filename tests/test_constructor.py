# Раздел «Конструктор». Проверка переходов к разделам: «Булки», «Соусы», «Начинки»
import pytest
import logging

from selenium.webdriver.support import expected_conditions as EC
from data.config import BASE_URL
from data.test_data import TAB_LOCATORS, rolls, sause, topping
from utils import get_ingredient, is_in_viewport, open_tab

logger = logging.getLogger(__name__)


# Тест переходов по табам и отображение первого элемента раздела
@pytest.mark.parametrize(
    "start_tab, target_tab, list_index, item_index",
    [
        (rolls, sause, 1, 0),  # Булки → Соус
        (rolls, topping, 2, 0),  # Булки → Начинки
        (sause, rolls, 0, 0),  # Соус → Булки
        (sause, topping, 2, 0),  # Соус → Начинки
        (topping, rolls, 0, 1),  # Начинки → Булки
        (topping, sause, 1, 1),  # Начинки → Соус
    ]
)
def test_tab_switch(browser, start_tab, target_tab, list_index, item_index):
    browser.get(BASE_URL)

    if start_tab != rolls:
        open_tab(browser, TAB_LOCATORS[start_tab])

    open_tab(browser, TAB_LOCATORS[target_tab])

    ingredient = get_ingredient(browser, list_index, item_index)
    logger.info(f"Найден элемент: {ingredient.text}")

    assert ingredient.is_displayed() and is_in_viewport(browser, ingredient), (
        f"{ingredient.text} - элемент вкладки '{target_tab}' не виден на экране"
    )
