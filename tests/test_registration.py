# Тесты на регистрацию пользователя
import pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.config import REGISTRATION_URL
from pages.locators import REGISTER_PAGE_LOCATORS

from data.test_data import VALID_USER
from utils import generate_email

logger = logging.getLogger(__name__)
class TestRegistration:

    # Тест успешной регистрации при валидных данных
    def test_register_success(self, browser):
        browser.get(REGISTRATION_URL)
        browser.find_element(
            *REGISTER_PAGE_LOCATORS["name"]).send_keys(VALID_USER["name"])
        new_login = generate_email()
        browser.find_element(
            *REGISTER_PAGE_LOCATORS["email"]).send_keys(new_login)
        logger.info(f"Сгенерированный логин: {new_login}")
        browser.find_element(
            *REGISTER_PAGE_LOCATORS["password"]).send_keys(VALID_USER["password"])
        browser.find_element(
            *REGISTER_PAGE_LOCATORS["register_button"]).click()
        WebDriverWait(browser, 5).until(
            EC.url_contains("/login")
        )

        assert "/login" in browser.current_url, "Не перешли на страницу логина!"

    # Тест ошибки для некорректного пароля (менее 6 символов)
    @pytest.mark.parametrize("invalid_pass, msg", [
        ('1', "Один символ"),
        ('123', "Три символа"),
        ('12345', "Пять символов")
    ])
    def test_register_invalid_password(self, browser, invalid_pass, msg):
        browser.get(REGISTRATION_URL)
        browser.find_element(
            *REGISTER_PAGE_LOCATORS["name"]).send_keys(VALID_USER["name"])
        browser.find_element(
            *REGISTER_PAGE_LOCATORS["email"]).send_keys(generate_email())
        browser.find_element(
            *REGISTER_PAGE_LOCATORS["password"]).send_keys(invalid_pass)
        browser.find_element(
            *REGISTER_PAGE_LOCATORS["register_button"]).click()

        error_element = browser.find_element(
            *REGISTER_PAGE_LOCATORS["password_error"])
        assert "Некорректный пароль" in error_element.text, "Ошибка не появилась!"
