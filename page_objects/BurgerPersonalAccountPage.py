from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PersonalAccountLocators:

    # Кнопка Профиль
    LOCATOR_ACCOUNT_PAGE_BUTTON_PROFILE = (By.XPATH, "//a[text()='Профиль']")
    # Кнопка Конструктор
    LOCATOR_ACCOUNT_PAGE_BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип Stellar Burgers
    LOCATOR_ACCOUNT_PAGE_LOGO = (By.XPATH, "//div[contains(@class, 'logo')]")
    # Кнопка выхода из аккаунта
    LOCATOR_ACCOUNT_PAGE_BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")


class PersonalAccountPage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/account/profile"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_button_constructor(self):
        self.find_element(PersonalAccountLocators.LOCATOR_ACCOUNT_PAGE_BUTTON_CONSTRUCTOR, time=10).click()

    def click_button_logo(self):
        self.find_element(PersonalAccountLocators.LOCATOR_ACCOUNT_PAGE_LOGO, time=10).click()

    def click_button_logout(self):
        self.find_element(PersonalAccountLocators.LOCATOR_ACCOUNT_PAGE_BUTTON_LOGOUT, time=10).click()
