# Тесты перехода по клику на «Конструктор» и на логотип Stellar Burgers

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import HEADERS_LOCATORS, MAIN_PAGE_LOCATORS, LOGIN_PAGE_LOCATORS

from data.config import BASE_URL

from utils import login_user, register_user


class TestLkHeaderLinks:

    # Неавторизованный пользователь
    # Тест на переход по клику на «Конструктор» из личного кабинета, неавторизованный пользователь
    def test_constructor_click_from_lk_guest(self, browser):
        browser.get(BASE_URL)
        browser.find_element(*HEADERS_LOCATORS["account_link"]).click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((LOGIN_PAGE_LOCATORS["h2_enter"])))
        browser.find_element(*HEADERS_LOCATORS["сonstructor"]).click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((MAIN_PAGE_LOCATORS["login_account_button"])))
        h1 = browser.find_element(*MAIN_PAGE_LOCATORS["h1_burgers"])
        assert BASE_URL == browser.current_url and h1.is_displayed(
        ), "Не перешли на страницу конструктора!"

    # Тест на переход по клику на логотип Stellar Burgers из личного кабинета, неавторизованный пользователь
    def test_logo_click_from_lk_guest(self, browser):
        browser.get(BASE_URL)
        browser.find_element(*HEADERS_LOCATORS["account_link"]).click()
        browser.find_element(*HEADERS_LOCATORS["logo"]).click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((MAIN_PAGE_LOCATORS["login_account_button"])))
        h1 = browser.find_element(*MAIN_PAGE_LOCATORS["h1_burgers"])
        assert BASE_URL == browser.current_url and h1.is_displayed(
        ), "Не перешли на страницу конструктора!"

    # Авторизованный пользователь
    # Тест на переход по клику на «Конструктор» из личного кабинета, авторизованный пользователь
    def test_constructor_click_from_lk_user(self, browser):
        email, password = register_user(browser)  # Регистрация пользователя
        browser.get(BASE_URL)
        ac_link = browser.find_element(
            *HEADERS_LOCATORS["account_link"])
        browser.execute_script("arguments[0].click();", ac_link)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((LOGIN_PAGE_LOCATORS["h2_enter"])))
        login_user(browser, email, password)      # Авторизация пользователя
        browser.find_element(*HEADERS_LOCATORS["account_link"]).click()
        con = browser.find_element(*HEADERS_LOCATORS["сonstructor"])
        browser.execute_script("arguments[0].click();", con)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((MAIN_PAGE_LOCATORS["order_button"])))
        h1 = browser.find_element(*MAIN_PAGE_LOCATORS["h1_burgers"])
        assert BASE_URL == browser.current_url and h1.is_displayed(
        ), "Не перешли на страницу конструктора!"

    # Тест на переход по клику на логотип Stellar Burgers из личного кабинета, авторизованный пользователь
    def test_logo_click_from_lk_user(self, browser):
        email, password = register_user(browser)  # Регистрация пользователя
        browser.get(BASE_URL)
        ac_link = browser.find_element(
            *HEADERS_LOCATORS["account_link"])
        browser.execute_script("arguments[0].click();", ac_link)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((LOGIN_PAGE_LOCATORS["h2_enter"])))
        login_user(browser, email, password)      # Авторизация пользователя
        browser.find_element(*HEADERS_LOCATORS["account_link"]).click()
        logo = browser.find_element(
            *HEADERS_LOCATORS["logo"])
        browser.execute_script("arguments[0].click();", logo)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((MAIN_PAGE_LOCATORS["order_button"])))
        h1 = browser.find_element(*MAIN_PAGE_LOCATORS["h1_burgers"])
        assert BASE_URL == browser.current_url and h1.is_displayed(
        ), "Не перешли на страницу конструктора!"
