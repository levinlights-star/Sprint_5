import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Для открытия и закрытия тестов в Chrome
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Для открытия и закрытия тестов в Chrome и в Firefox
# @pytest.fixture(scope="function", params=["chrome", "firefox"])
# def browser(request):
    # if request.param == "chrome":
    #     driver = webdriver.Chrome()
    # else:
    #     driver = webdriver.Firefox()
    # yield driver
    # driver.quit()
