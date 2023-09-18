from page_objects.BurgerConstructorPage import ConstructorPage, ConstructorLocators
from page_objects.BurgerEntrancePage import EntrancePage, EntranceLocators
from page_objects.BurgerPersonalCabinetPage import PersonalAccountPage, PersonalAccountLocators
import allure

@allure.title("Transfer to personal account")
@allure.description("Checking the transition to the personal account by clicking the button.")
def test_transfer_to_personal_account(browser):
    main_account_page = PersonalAccountPage(browser)
    main_account_page.transfer_to_personal_account(browser)
    assert main_account_page.find_element(PersonalAccountLocators.LOCATOR_ACCOUNT_PAGE_BUTTON_PROFILE)
    assert main_account_page.driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"


@allure.title("Transfer to constructor via button")
@allure.description("The transition from the personal account to the constructor by clicking the button.")
def test_transfer_to_constructor_via_button(browser):
    main_constructor_page = ConstructorPage(browser)
    main_entrance_page = EntrancePage(browser)
    main_account_page = PersonalAccountPage(browser)
    main_account_page.transfer_to_personal_account(browser)
    assert main_account_page.find_element(PersonalAccountLocators.LOCATOR_ACCOUNT_PAGE_BUTTON_PROFILE)
    assert main_account_page.driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
    main_account_page.click_button_constructor()
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_BUNS)
    assert main_entrance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/"


@allure.title("Transfer to constructor via logo")
@allure.description("The transition from the personal account to the constructor by clicking the logo.")
def test_transfer_to_constructor_via_logo(browser):
    main_constructor_page = ConstructorPage(browser)
    main_entrance_page = EntrancePage(browser)
    main_account_page = PersonalAccountPage(browser)
    main_account_page.transfer_to_personal_account(browser)
    assert main_account_page.find_element(PersonalAccountLocators.LOCATOR_ACCOUNT_PAGE_BUTTON_PROFILE)
    assert main_account_page.driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
    main_account_page.click_button_logo()
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_BUNS)
    assert main_entrance_page.driver.current_url == "https://stellarburgers.nomoreparties.site/"


@allure.title("logout account")
@allure.description("Checking the account logout.")
def test_logout_account(browser):
    main_entrance_page = EntrancePage(browser)
    main_account_page = PersonalAccountPage(browser)
    main_account_page.transfer_to_personal_account(browser)
    assert main_account_page.find_element(PersonalAccountLocators.LOCATOR_ACCOUNT_PAGE_BUTTON_PROFILE)
    assert main_account_page.driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
    main_account_page.click_button_logout()
    assert main_entrance_page.find_element(EntranceLocators.LOCATOR_ENTANCE_PAGE_CAPTION)
    assert main_account_page.driver.current_url == "https://stellarburgers.nomoreparties.site/login"

