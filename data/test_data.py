from pages.locators import MAIN_PAGE_LOCATORS

VALID_USER = {
    "name": "tests",
    "email": "tests_1@yandex.ru",
    "password": "123456"
}


rolls = "Булки"
sause = "Соусы"
topping = "Начинки"

TAB_LOCATORS = {
    rolls: MAIN_PAGE_LOCATORS["rolls_tab"],
    sause: MAIN_PAGE_LOCATORS["sauses_tab"],
    topping: MAIN_PAGE_LOCATORS["topping_tab"],
}