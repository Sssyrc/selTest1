from pages.main_page import MainPage
import locators.main_page_locators as mp


def test_hot_tours(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.check_text(mp.HOT_TOURS_TITLE_XPATH)

def test_popular_tours_sea(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.check_text(mp.POPULAR_TOURS_SEA_FILTER_XPATH)

def test_popular_tours_tropic(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.check_text(mp.POPULAR_TOURS_TROPIC_FILTER_XPATH)

def test_popular_tours_asia(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.check_text(mp.POPULAR_TOURS_ASIA_FILTER_XPATH)

def test_popular_tours_europe(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.check_text(mp.POPULAR_TOURS_EUROPE_FILTER_XPATH)