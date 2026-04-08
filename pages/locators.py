from selenium.webdriver.common.by import By

# Локаторы для шапки сайта
HEADERS_LOCATORS = {
    # Конструктор
    "сonstructor": (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and contains(text(), 'Конструктор')]"),
    # Лента заказов
    "feed": (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and contains(text(), 'Лента Заказов')]"),
    # Клик по лого
    "logo": (By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2 a"),
    # Личный кабинет
    "account_link": (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and contains(text(), 'Личный Кабинет')]")
}


# Локаторы для страницы регистрации пользователя {BASE_URL}/register
REGISTER_PAGE_LOCATORS = {
    # Форма регистрации
    # Имя
    "name": (By.XPATH, "//label[contains(text(), 'Имя')]/following::input"),
    # Email
    "email": (By.XPATH, "//label[contains(text(),'Email')]/following::input"),
    # Пароль
    "password": (By.XPATH, "//label[contains(text(),'Пароль')]/following::input"),
    # Зарегистрироваться кнопка
    "register_button": (By.XPATH, "//button[text()='Зарегистрироваться']"),
    # Ошибка "Неверный пароль"
    "password_error": (By.XPATH, "//p[contains(@class, 'input__error')]"),

    # Войти (ссылка под формой регистрации)
    "enter_account_link": (By.XPATH, '//a[contains(@class, "Auth_link") and contains(text(), "Войти")]'),
    # Заголовок h2 "Регистрация"
    "h2_register": (By.XPATH, "//h2[contains(text(),'Регистрация')]"),
}


# Локаторы на главной странице
MAIN_PAGE_LOCATORS = {
    # Кнопка "Войти в аккаунт", доступна неавторизованному пользователю
    "login_account_button": (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Войти в аккаунт')]"),
    # Кнопка "Оформить заказ", доступна авторизованному пользователю
    "order_button": (By.XPATH, "//button[text()='Оформить заказ']"),
    # Заголовок "Соберите бургер"
    "h1_burgers": (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"),
    # Табы ингридиетов (Булки/Соусы/Начинки)
    "ingridient_list": (By.CSS_SELECTOR, "ul[class*='BurgerIngredients_ingredients__list']"),
    # Булки
    "rolls_tab": (By.XPATH, '//span[text()="Булки"]'),
    # Соусы
    "sauses_tab": (By.XPATH, '//span[text()="Соусы"]'),
    # Начинки
    "topping_tab": (By.XPATH, '//span[text()="Начинки"]')
}


# Локаторы на странице авторизации {BASE_URL}/login
LOGIN_PAGE_LOCATORS = {
    # Форма авторизации
    # Заголовок "Вход"
    "h2_enter": (By.XPATH, "//h2[contains(text(),'Вход')]"),
    # Email 
    "email": (By.XPATH, "//label[contains(text(),'Email')]/following::input"),
    # Пароль
    "password": (By.XPATH, "//label[contains(text(),'Пароль')]/following::input"),
    # Кнопка "Войти"
    "enter_button": (By.XPATH, "//button[text()='Войти']")
}


# Локаторы на странице редактирования профиля {BASE_URL}/account/profile
PROFILE_PAGE_LOCATORS = {
    # Кнопка "Сохранить"
    "save_button": (By.XPATH, "//button[contains(text(), 'Сохранить')]"),
    # Кнопка "Выйти"
    "exit_button": (By.XPATH, '//button[text()="Выход"]')
}


# Локаторы на странице восстановления пароля {BASE_URL}/forgot-password
FORGOT_PAGE_LOCATORS = {
    # Ссылка с текстом "Войти" под формой восстановления пароля
    "enter_reg_account_link": (
        By.XPATH,
        '//a[contains(@class, "Auth_link") and contains(text(), "Войти")]'
    ),

}
