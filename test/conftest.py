import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(params=["chrome", "yandex"])
def browser(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif request.param == "yandex":
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/yandex-browser'
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager("114.0.5735.685").install()), options=options)
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
