from selenium.webdriver.common.by import By
from pages.base_page import BasePage

import locators.base_locators

class MainPage(BasePage):

    def open_main_page(self):
        self.driver.get(locators.base_locators.BASE_URL)

    def check_text(self, locator):
        assert self.driver.find_element(By.XPATH, locator).is_displayed()

