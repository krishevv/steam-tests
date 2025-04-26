from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from utils.config import config
from pages.base_page import BasePage

class MainPage(BasePage):
    URL = config.get("base_url")
    __ABOUT_BUTTON = (By.XPATH, "//*[@class='supernav_container']/a[@class='menuitem ' and contains(text(), 'About')]")  
    __NEW_AND_NOTEWORTHY = (By.XPATH, "//*[@class = 'pulldown']/a[contains(text(),'New')][1]")
    __TOP_SELLERS = (By.XPATH, "//a[@class = 'popup_menu_item' and contains(@href,'topselling')]")
    
    def open(self):
        self.open_url(self.URL)

    def click_about(self):
        about_button = self.wait.until(EC.visibility_of_element_located(self.__ABOUT_BUTTON))
        about_button.click()
    
    def hover_and_wait_for_popup(self):

        new_and_noteworthy = self.find_element(self.__NEW_AND_NOTEWORTHY)
        ActionChains(self.driver).move_to_element(new_and_noteworthy).perform()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.__TOP_SELLERS)
        )
    
    
    def click_best_sellers(self):
        
        self.click_element(self.__TOP_SELLERS)