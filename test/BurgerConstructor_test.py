from page_objects.BurgerConstructorPage import ConstructorPage, ConstructorLocators
import allure
@allure.title("Navigating through sections")
@allure.description("Navigation through sections of the main page.")
def test_navigating_through_sections(browser):
    main_constructor_page = ConstructorPage(browser)
    main_constructor_page.go_to_constructor_page()
    main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_BUTTON_CONSTRUCTOR)
    main_constructor_page.click_button_toppings()
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_CAPTION_TOPPINGS)
    main_constructor_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    main_constructor_page.click_button_buns()
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_CAPTION_BUNS)
    main_constructor_page.click_button_sauces()
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_CAPTION_SAUCES)
    main_constructor_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")




