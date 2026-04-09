import random
import logging

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import LOGIN_PAGE_LOCATORS, MAIN_PAGE_LOCATORS, REGISTER_PAGE_LOCATORS

from data.test_data import VALID_USER

from data.config import BASE_URL, REGISTRATION_URL

logger = logging.getLogger(__name__)

# Функция авторизации пользователя на странице {BASE_URL}login
def login_user(browser, email, password):
    browser.find_element(*LOGIN_PAGE_LOCATORS["email"]).send_keys(email)
    browser.find_element(*LOGIN_PAGE_LOCATORS["password"]).send_keys(password)

    enter_button = browser.find_element(*LOGIN_PAGE_LOCATORS["enter_button"])
    browser.execute_script("arguments[0].click();", enter_button)

    WebDriverWait(browser, 10).until(EC.url_to_be(BASE_URL))


# Функция для регистрации пользователя
def register_user(browser):
    browser.get(REGISTRATION_URL)

    browser.find_element(
        *REGISTER_PAGE_LOCATORS["name"]).send_keys(VALID_USER["name"])
    login = generate_email()
    browser.find_element(*REGISTER_PAGE_LOCATORS["email"]).send_keys(login)
    logger.info(f"Сгенерированный логин: {login}")
    password = VALID_USER["password"]
    browser.find_element(
        *REGISTER_PAGE_LOCATORS["password"]).send_keys(password)
    browser.find_element(*REGISTER_PAGE_LOCATORS["register_button"]).click()

    WebDriverWait(browser, 5).until(EC.url_contains("/login"))
    return login, password


# Функция для генерации email
DOMAINS = ['mail.ru', 'yandex.ru', 'gmail.com']


def generate_email():
    body = str(random.randint(000, 999)).zfill(3)
    domain = random.choice(DOMAINS)
    return f"Vitenkova_44_{body}@{domain}"


# Область видимости в браузере
def is_in_viewport(browser, element):
    return browser.execute_script("""
        const rect = arguments[0].getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= window.innerHeight &&
            rect.right <= window.innerWidth
        );
    """, element)


# Выбор элемента продукта в конструкторе бургеров
def get_ingredient(browser, list_index, item_index):
    uls = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located(
            MAIN_PAGE_LOCATORS["ingridient_list"])
    )
    ingredient_ul = uls[list_index]
    ingredient_links = ingredient_ul.find_elements(By.TAG_NAME, "a")
    return ingredient_links[item_index]


# Функция клика по табам в конструкторе бургера
def open_tab(browser, tab_locator):
    tab = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(tab_locator))
    browser.execute_script("arguments[0].click();", tab)
