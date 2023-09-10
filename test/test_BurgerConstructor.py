from page_objects.BurgerConstructorPage import ConstructorPage, ConstructorLocators


def test_section(browser):
    main_constructor_page = ConstructorPage(browser)
    main_constructor_page.go_to_site()
    main_constructor_page.click_button_sauces()
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_CAPTION_SAUCES)
    main_constructor_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    main_constructor_page.click_button_buns()
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_CAPTION_BUNS)
    main_constructor_page.click_button_toppings()
    assert main_constructor_page.find_element(ConstructorLocators.LOCATOR_CONSTRUCTOR_PAGE_CAPTION_TOPPINGS)


