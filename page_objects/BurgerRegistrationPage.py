from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class RegistrationLocators:

    # Поле для ввода имени
    LOCATOR_REGISTRATION_PAGE_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле для ввода email
    LOCATOR_REGISTRATION_PAGE_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле для ввода пароля
    LOCATOR_REGISTRATION_PAGE_PASSWORD = (By.XPATH, "//input[@type='password']")
    # Кнопка Зарегистрироваться
    LOCATOR_REGISTRATION_PAGE_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Сообщение неккоректный пароль
    LOCATOR_REGISTRATION_PAGE_ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")
    # Ссылка Войти
    LOCATOR_REGISTRATION_PAGE_BUTTON_ENTANCE = (By.XPATH, "//a[text()='Войти']")

class RegistrationPage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/register"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_registration_page(self):
        return self.driver.get(self.base_url)

    def filling_registration_form(self, name, email, password):
        self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_PAGE_NAME, time=10).send_keys(name)
        self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_PAGE_EMAIL, time=10).send_keys(email)
        self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_PAGE_PASSWORD, time=10).send_keys(password)
        self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_PAGE_BUTTON, time=10).click()

    def click_button_sign(self):
        self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_PAGE_BUTTON_ENTANCE, time=10).click()


