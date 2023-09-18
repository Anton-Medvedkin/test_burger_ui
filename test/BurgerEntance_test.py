from page_objects.BurgerConstructorPage import ConstructorPage, ConstructorLocators
from page_objects.BurgerEntancePage import EntancePage, EntanceLocators
from page_objects.BurgerRegistrationPage import RegistrationPage, RegistrationLocators
from page_objects.BurgerRestorePasswordPage import RestorePasswordPage, RestorePasswordLocators
import allure

@allure.title("Login via home page")
@allure.description("Log in using the Log in to account button on the home page.")
def test_login_via_home_page(browser):
    main_constructor_page = ConstructorPage(browser)
    main_constructor_page.go_to_constructor_page()
    main_constructor_page.click_button_entance()
    main_entance_page = EntancePage(browser)
    assert main_entance_page.find_element(EntanceLocators.LOCATOR_ENTANCE_PAGE_CAPTION)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    main_entance_page.filling_entance_form("medvetdhek.ant@yandex.by", "123h45te67")
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_BUNS)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/"

@allure.title("Login via personal account")
@allure.description("Login via the Personal Account button.")
def test_login_via_personal_account(browser):
    main_constructor_page = ConstructorPage(browser)
    main_constructor_page.go_to_constructor_page()
    main_constructor_page.click_button_personal_cabinet()
    main_entance_page = EntancePage(browser)
    assert main_entance_page.find_element(EntanceLocators.LOCATOR_ENTANCE_PAGE_CAPTION)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    main_entance_page.filling_entance_form("medvetdhek.ant@yandex.by", "123h45te67")
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_BUNS)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/"


@allure.title("Login via registration form")
@allure.description("Login via the button on the registration form.")
def test_login_via_registration_form(browser):
    main_registration_page = RegistrationPage(browser)
    main_registration_page.go_to_registration_page()
    main_registration_page.click_button_sign()
    main_entance_page = EntancePage(browser)
    assert main_entance_page.find_element(EntanceLocators.LOCATOR_ENTANCE_PAGE_CAPTION)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    main_entance_page.filling_entance_form("medvetdhek.ant@yandex.by", "123h45te67")
    main_constructor_page = ConstructorPage(browser)
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_BUNS)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/"


@allure.title("Login via restore password form")
@allure.description("Login via the button on the password recovery form.")
def test_login_via_restore_password_form(browser):
    main_restore_page = RestorePasswordPage(browser)
    main_restore_page.go_to_restore_password_page()
    main_restore_page.click_button_entance()
    main_entance_page = EntancePage(browser)
    assert main_entance_page.find_element(EntanceLocators.LOCATOR_ENTANCE_PAGE_CAPTION)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    main_entance_page.filling_entance_form("medvetdhek.ant@yandex.by", "123h45te67")
    main_constructor_page = ConstructorPage(browser)
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_BUNS)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/"




