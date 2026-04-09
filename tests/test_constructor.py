# Раздел «Конструктор». Проверка переходов к разделам: «Булки», «Соусы», «Начинки»
import pytest
import logging

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from data.config import BASE_URL

from pages.locators import MAIN_PAGE_LOCATORS

from utils import get_ingredient, is_in_viewport, open_tab

logger = logging.getLogger(__name__)


# Тест на клик со вкладки Булки на Соусы и Начинка + проверка отображения элементов после автоскролла
@pytest.mark.parametrize(
    "target_tab, list_index, item_index",
    [
        (MAIN_PAGE_LOCATORS["sauses_tab"], 0, 0),  # Булки → Соус
        (MAIN_PAGE_LOCATORS["topping_tab"], 2, 0)  # Булки → Начинки
    ]
)
def test_tab_switch_from_rolls(browser, target_tab, list_index, item_index):
    browser.get(BASE_URL)

    open_tab(browser, target_tab)
    logger.info(f"Открыт таб {target_tab}")

    ingredient = get_ingredient(browser, list_index, item_index)

    logger.info(f"Найден элемент: {ingredient.text}")

    WebDriverWait(browser, 5).until(
        lambda d: d.execute_script("""
        const r = arguments[0].getBoundingClientRect();
        return r.top >= 0 && r.bottom <= window.innerHeight;
    """, ingredient)
    )

    assert ingredient.is_displayed() and is_in_viewport(browser, ingredient), (
        f"{ingredient.text} - элемент вкладки '{target_tab}' не виден на экране"
    )

# Тест на клик со вкладки Соусы и Начинки на Булки, Соусы, Начинка + проверка отображения элементов после автоскролла
@pytest.mark.parametrize(
    "start_tab, target_tab, list_index, item_index",
    [
        # Соус → Булки
        (MAIN_PAGE_LOCATORS["sauses_tab"],
         MAIN_PAGE_LOCATORS["rolls_tab"], 0, 0),
        # Соус → Начинки
        (MAIN_PAGE_LOCATORS["sauses_tab"],
         MAIN_PAGE_LOCATORS["topping_tab"], 2, 0),
        # Начинки → Булки
        (MAIN_PAGE_LOCATORS["topping_tab"],
         MAIN_PAGE_LOCATORS["rolls_tab"], 0, 0),
        # Начинки → Соусы
        (MAIN_PAGE_LOCATORS["topping_tab"],
         MAIN_PAGE_LOCATORS["sauses_tab"], 1, 0)
    ]
)
def test_tab_switch_from_sause(browser, start_tab, target_tab, list_index, item_index):
    browser.get(BASE_URL)

    open_tab(browser, start_tab)
    logger.info(f"Вкладка {start_tab}")
    open_tab(browser, target_tab)
    logger.info(f"Открыта вкладка {target_tab}")

    ingredient = get_ingredient(browser, list_index, item_index)

    logger.info(f"Найден элемент: {ingredient.text}")

    WebDriverWait(browser, 5).until(
        lambda d: d.execute_script("""
        const r = arguments[0].getBoundingClientRect();
        return r.top >= 0 && r.bottom <= window.innerHeight;
    """, ingredient)
    )

    assert ingredient.is_displayed() and is_in_viewport(browser, ingredient), (
        f"{ingredient.text} - элемент вкладки '{target_tab}' не виден на экране"
    )
