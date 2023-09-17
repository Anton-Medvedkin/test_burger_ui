from page_objects.BurgerConstructorPage import ConstructorPage, ConstructorLocators
from page_objects.BurgerEntancePage import EntancePage, EntanceLocators
from page_objects.BurgerRegistrationPage import RegistrationPage, RegistrationLocators
from page_objects.BurgerRestorePasswordPage import RestorePasswordPage, RestorePasswordLocators

def test_sign_in_account_button_on_the_home_page(browser):
    main_constructor_page = ConstructorPage(browser)
    main_constructor_page.go_to_constructor_page()
    main_constructor_page.click_button_entance()
    main_entance_page = EntancePage(browser)
    assert main_entance_page.find_element(EntanceLocators.LOCATOR_ENTANCE_PAGE_CAPTION)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    main_entance_page.filling_entance_form("medvetdhek.ant@yandex.by", "123h45te67")
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_BUNS)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/"

def test_sign_in_personal_account_button(browser):
    main_constructor_page = ConstructorPage(browser)
    main_constructor_page.go_to_constructor_page()
    main_constructor_page.click_button_personal_cabinet()
    main_entance_page = EntancePage(browser)
    assert main_entance_page.find_element(EntanceLocators.LOCATOR_ENTANCE_PAGE_CAPTION)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    main_entance_page.filling_entance_form("medvetdhek.ant@yandex.by", "123h45te67")
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_BUNS)
    assert main_entance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/"

def test_sign_in_registration_form(browser):
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

def test_sign_in_restore_password_form(browser):
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




