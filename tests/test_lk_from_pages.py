# Тесты перехода по клику на «Личный кабинет»

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.config import BASE_URL, LOGIN_URL, ORDER_FEED_URL, REGISTRATION_URL, FORGOT_PAS_URL, PROFILE_URL

from pages.locators import MAIN_PAGE_LOCATORS, LOGIN_PAGE_LOCATORS, HEADERS_LOCATORS, PROFILE_PAGE_LOCATORS

from utils import login_user, register_user


class TestLkFromPages:

    # Тест на переход по "Личный кабинет" в шапке сайта с разных страниц, неавторизованный пользователь
    @pytest.mark.parametrize("url, msg", [
        (BASE_URL, "Главная страница"),              # Главная → Личный кабинет
        (ORDER_FEED_URL, "стр. Лента заказов"),      # Лента заказов → Личный кабинет
        (LOGIN_URL, "стр. Личный кабинет"),          # Личный кабинет → Личный кабинет        
        (REGISTRATION_URL, "стр. Регистрация"),      # Регистрация → Личный кабинет
        (FORGOT_PAS_URL, "стр. Восстановить пароль") # Восстановление пароля → Личный кабинет
    ])
    def test_lk_from_guest_to_login(self, browser, url, msg):
        browser.get(url)
        browser.find_element(*HEADERS_LOCATORS["account_link"]).click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((LOGIN_PAGE_LOCATORS["h2_enter"])))
        visible_button = browser.find_element(
            *LOGIN_PAGE_LOCATORS["enter_button"])
        assert LOGIN_URL == browser.current_url and visible_button.is_displayed(
        ), "Не перешли на страницу логина!"

    # Тест на переход по "Личный кабинет" в шапке сайта с разных страниц, авторизованный пользователь
    @pytest.mark.parametrize("url, msg", [
        (BASE_URL, "Главная страница"),              # Главная → Личный кабинет        
        (ORDER_FEED_URL, "стр. Лента заказов"),      # Лента заказов → Личный кабинет      
        (REGISTRATION_URL, "стр. Регистрация"),      # Регистрация → Личный кабинет        
        (FORGOT_PAS_URL, "стр. Восстановить пароль") # Восстановление пароля → Личный кабинет
    ])
    def test_lk_from_user_to_account(self, browser, url, msg):
        email, password = register_user(browser)  # Регистрация пользователя
        browser.get(LOGIN_URL)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((LOGIN_PAGE_LOCATORS["h2_enter"])))
        login_user(browser, email, password)      # Авторизация пользователя
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((MAIN_PAGE_LOCATORS["order_button"])))
        browser.get(url)
        ac_link = browser.find_element(
            *HEADERS_LOCATORS["account_link"])
        browser.execute_script("arguments[0].click();", ac_link)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((PROFILE_PAGE_LOCATORS["save_button"])))
        visible_button = browser.find_element(
            *PROFILE_PAGE_LOCATORS["save_button"])
        assert PROFILE_URL == browser.current_url and visible_button.is_displayed(
        ), "Не перешли на страницу редактирования профиля!"
