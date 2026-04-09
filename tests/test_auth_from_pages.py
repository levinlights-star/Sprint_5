# Тесты на проверку входа в аккаунт с разных страниц

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.config import BASE_URL, REGISTRATION_URL, FORGOT_PAS_URL

from pages.locators import HEADERS_LOCATORS, MAIN_PAGE_LOCATORS, LOGIN_PAGE_LOCATORS, REGISTER_PAGE_LOCATORS, FORGOT_PAGE_LOCATORS

from utils import login_user, register_user


class TestAuth:

    # Тест входа по кнопке «Войти в аккаунт» на главной
    def test_login_from_account_btn(self, browser):
        email, password = register_user(browser)  # Регистрация пользователя
        browser.get(BASE_URL)
        log_btn = browser.find_element(
            *MAIN_PAGE_LOCATORS["login_account_button"])
        browser.execute_script("arguments[0].click();", log_btn)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((LOGIN_PAGE_LOCATORS["h2_enter"])))

        login_user(browser, email, password)      # Авторизация пользователя

        # проверяем переход на гл. страницу и наличие кнопки "Оформить заказ"
        vis_btn = browser.find_element(*MAIN_PAGE_LOCATORS["order_button"])
        assert BASE_URL == browser.current_url and vis_btn.is_displayed(
        ), "Не перешли на страницу логина!"

    # Тест входа через кнопку «Личный кабинет»
    def test_login_from_lk_btn(self, browser):
        email, password = register_user(browser)  # Регистрация пользователя
        browser.get(BASE_URL)
        ac_link = browser.find_element(
            *HEADERS_LOCATORS["account_link"])
        browser.execute_script("arguments[0].click();", ac_link)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((LOGIN_PAGE_LOCATORS["h2_enter"])))

        login_user(browser, email, password)      # Авторизация пользователя

        vis_btn = browser.find_element(*MAIN_PAGE_LOCATORS["order_button"])
        assert BASE_URL == browser.current_url and vis_btn.is_displayed(
        ), "Не перешли на страницу логина!"

    # Тест входа через кнопку в форме регистрации
    def test_login_from_register_btn(self, browser):
        email, password = register_user(browser)  # Регистрация пользователя
        browser.get(REGISTRATION_URL)
        acc_link = browser.find_element(
            *REGISTER_PAGE_LOCATORS["enter_account_link"])
        browser.execute_script("arguments[0].click();", acc_link)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((LOGIN_PAGE_LOCATORS["h2_enter"])))

        login_user(browser, email, password)      # Авторизация пользователя

        # проверяем переход на гл. страницу и наличие кнопки "Оформить заказ"
        vis_btn = browser.find_element(*MAIN_PAGE_LOCATORS["order_button"])
        assert BASE_URL == browser.current_url and vis_btn.is_displayed(
        ), "Не перешли на страницу логина!"

    # Тест входа через кнопку в форме восстановления пароля
    def test_login_from_forgot_btn(self, browser):
        email, password = register_user(browser)  # Регистрация пользователя
        browser.get(FORGOT_PAS_URL)
        reg_link = browser.find_element(
            *FORGOT_PAGE_LOCATORS["enter_reg_account_link"])
        browser.execute_script("arguments[0].click();", reg_link)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((LOGIN_PAGE_LOCATORS["h2_enter"])))

        login_user(browser, email, password)      # Авторизация пользователя

        vis_btn = browser.find_element(*MAIN_PAGE_LOCATORS["order_button"])
        assert BASE_URL == browser.current_url and vis_btn.is_displayed(
        ), "Не перешли на страницу логина!"
