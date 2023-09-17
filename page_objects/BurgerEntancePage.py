from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class EntanceLocators:

    #Поле для ввода email
    LOCATOR_ENTANCE_PAGE_EMAIL = (By.XPATH, "//input[@type='text']")
    #Поле для ввода пароля
    LOCATOR_ENTANCE_PAGE_PASSWORD = (By.XPATH, "//input[@type='password']")
    #Кнопка Войти
    LOCATOR_ENTANCE_PAGE_BUTTON = (By.XPATH, "//button[text()='Войти']")
    #Заголовок Вход
    LOCATOR_ENTANCE_PAGE_CAPTION = (By.XPATH, "//h2[text()='Вход']")
    # Кнопка Восстановить пароль
    LOCATOR_ENTANCE_PAGE_BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")



class EntancePage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_entance_page(self):
        return self.driver.get(self.base_url)

    def filling_entance_form(self, email, password):
        self.find_element(EntanceLocators.LOCATOR_ENTANCE_PAGE_EMAIL, time=10).send_keys(email)
        self.find_element(EntanceLocators.LOCATOR_ENTANCE_PAGE_PASSWORD, time=10).send_keys(password)
        self.find_element(EntanceLocators.LOCATOR_ENTANCE_PAGE_BUTTON, time=10).click()