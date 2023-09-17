from page_objects.BurgerRegistrationPage import RegistrationPage, RegistrationLocators
from page_objects.BurgerEntancePage import EntancePage, EntanceLocators


def test_successful_registration(browser, create_user):
    main_registration_page = RegistrationPage(browser)
    main_registration_page.go_to_registration_page()
    main_registration_page.filling_registration_form("AntoName", "medved.email@yandex.by", "123456ggg")
    main_entance_page = EntancePage(browser)
    assert main_entance_page.find_element(EntanceLocators.LOCATOR_ENTANCE_PAGE_CAPTION)
    assert main_registration_page.driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_registration_with_invalid_password(browser):
    main_registration_page = RegistrationPage(browser)
    main_registration_page.go_to_registration_page()
    main_registration_page.filling_registration_form("Antonyjte", "medvetdhek.ant@yandex.by", "123")
    assert main_registration_page.find_element(RegistrationLocators.LOCATOR_REGISTRATION_PAGE_ERROR_MESSAGE)
    assert main_registration_page.driver.current_url == "https://stellarburgers.nomoreparties.site/register"