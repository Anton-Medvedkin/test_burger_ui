from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ConstructorLocators:

    # Кнопка конструктор
    LOCATOR_CONSTRUCTOR_PAGE_BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    # Кнопка Личный Кабинет
    LOCATOR_CONSTRUCTOR_PAGE_BUTTON_PERSONAL_CABINET = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Кнопка Войти в аккаунт
    LOCATOR_CONSTRUCTOR_PAGE_BUTTON_SIGN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка Булки
    LOCATOR_CONSTRUCTOR_PAGE_BUTTON_BUNS = (By.XPATH, "//span[text()='Булки']")
    # Кнопка Соусы
    LOCATOR_CONSTRUCTOR_PAGE_BUTTON_SAUCES = (By.XPATH, "//span[text()='Соусы']")
    # Кнопка Начинки
    LOCATOR_CONSTRUCTOR_PAGE_BUTTON_TOPPINGS = (By.XPATH, "//span[text()='Начинки']")
    # Заголовок Булки
    LOCATOR_CONSTRUCTOR_PAGE_CAPTION_BUNS = (By.XPATH, "//h2[text()='Булки']")
    # Заголовок Соусы
    LOCATOR_CONSTRUCTOR_PAGE_CAPTION_SAUCES = (By.XPATH, "//h2[text()='Соусы']")
    # Заголовок Начинки
    LOCATOR_CONSTRUCTOR_PAGE_CAPTION_TOPPINGS = (By.XPATH, "//h2[text()='Начинки']")



class ConstructorPage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_constructor_page(self):
        return self.driver.get(self.base_url)

    def click_button_entance(self):
        self.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_SIGN, time=10).click()

    def click_button_personal_cabinet(self):
        self.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_PERSONAL_CABINET, time=10).click()

    def click_button_buns(self):
        self.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_BUNS, time=20).click()

    def click_button_sauces(self):
        self.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_SAUCES, time=20).click()

    def click_button_toppings(self):
        self.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_TOPPINGS, time=20).click()