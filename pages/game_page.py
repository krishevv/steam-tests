from selenium.webdriver.common.by import By
from pages.base_page import BasePage  

class GamePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    __TITLE_LOCATOR = (By.XPATH, "//*[@id='appHubAppName']")
    __PRICE_LOCATOR = (By.XPATH, "(//*[contains(@class, 'game_purchase_price')])[1]")
    __RELEASE_DATE_LOCATOR = (By.XPATH, "(//div[@class='date'])[1]")


    def get_game_title(self):
        
        return self.get_text(self.__TITLE_LOCATOR)

    def get_game_price(self):

        return self.get_text(self.__PRICE_LOCATOR)

    def get_game_release_date(self):

        return  self.get_text(self.__RELEASE_DATE_LOCATOR)