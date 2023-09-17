from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class RestorePasswordLocators:

    #Ссылка Войти
    LOCATOR_RESTORE_PAGE_BUTTON_ENTANCE = (By.XPATH, "//a[text()='Войти']")


class RestorePasswordPage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/forgot-password"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_restore_password_page(self):
        return self.driver.get(self.base_url)

    def click_button_entance(self):
        self.find_element(RestorePasswordLocators.LOCATOR_RESTORE_PAGE_BUTTON_ENTANCE, time=10).click()