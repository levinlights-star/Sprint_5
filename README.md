# Sprint_5
Структура проекта

Sprint_5/
├── tests/
│   └── test_auth_from_pages.py                    # Тесты на проверку входа в аккаунт с разных страниц
│   └── test_constructor.py                        # Тесты переходов по конструктору бургеров
│   └── test_lk_from_pages.py                      # Тесты перехода по клику на «Личный кабинет»
│   └── test_lk_header_links.py                    # Тесты перехода по клику на «Конструктор» и на логотип Stellar Burgers
│   └── test_logout.py                             # Тест на выход из аккаунта по кнопке «Выйти» в личном кабинете
│   └── test_registration.py                       # Тесты на регистрацию пользователя
│ 
├── conftest.py                                    # Фикстуры
├── utils.py                                       # Функция
├── pytest.ini
├── .gitignore
├── README.md
│ 
├── pages
│   ├── locators.py                                # Локаторы для страниц
└── data/
    ├── config.py                                  # URL сайта
    └── test_data.py                               # Тестовые данные


Запуск всех тестов: pytest tests -v

Пример выполнения: pytest tests\test_registration.py::TestRegistration::test_register_success -v
tests/test_registration.py::TestRegistration::test_register_success
----------------------------------------------------------------------------------- live log call ------------------------------------------------------------------------------------
INFO     test_registration:test_registration.py:24 Сгенерированный логин: Vitenkova_44_630@mail.ru
PASSED                                                                                                                                                                          [100%]

================================================================================= 1 passed in 7.35s 