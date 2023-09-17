import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=["chrome", "yandex"])
def browser(request):
    if request.param == "chrome":
        ChromeDriverManagerdriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        #service = Service(executable_path='./chromedriver.txt')
        #driver = webdriver.Chrome(service=service, options=options)
        #driver.maximize_window()
    elif request.param == "yandex":
        # options = webdriver.ChromeOptions()
        # binary_yandex_driver_file = 'yandexdriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome()
    else:
        raise ValueError("Неподдерживаемый браузер")
    yield driver
    driver.quit()

@pytest.fixture()
def create_user():
    json_data = {
        "email": "medved.email@yandex.by",
        "password": "123456ggg"
    }
    yield json_data
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", data=json_data)
    response_token = response.json()['accessToken']
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)
