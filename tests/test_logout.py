from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import HEADERS_LOCATORS, LOGIN_PAGE_LOCATORS, PROFILE_PAGE_LOCATORS

from data.config import LOGIN_URL

from utils import login_user, register_user


class TestLogout:
    # Тест на выход из аккаунта по кнопке «Выйти» в личном кабинете
    def test_successful_logout(self, browser):
        email, password = register_user(browser)  # Регистрация пользователя

        browser.get(LOGIN_URL)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((LOGIN_PAGE_LOCATORS["h2_enter"])))

        login_user(browser, email, password)  # Авторизация пользователя
        browser.find_element(*HEADERS_LOCATORS["account_link"]).click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((PROFILE_PAGE_LOCATORS["save_button"])))

        exit_button = browser.find_element(
            *PROFILE_PAGE_LOCATORS["exit_button"])
        browser.execute_script("arguments[0].click();", exit_button)

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((LOGIN_PAGE_LOCATORS["h2_enter"])))
        vis_btn = browser.find_element(*LOGIN_PAGE_LOCATORS["enter_button"])
        assert LOGIN_URL == browser.current_url and vis_btn.is_displayed(
        ), "Не вышли из аккаунта!"
