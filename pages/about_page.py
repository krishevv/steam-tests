from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AboutPage(BasePage):
    __CURRENT_PLAYERS = (By.XPATH, "//*[@class='online_stat_label gamers_in_game']/ancestor::*[@class='online_stat']") 
    __PEAK_PLAYERS = (By.XPATH, "//*[@class='online_stat_label gamers_online']/ancestor::*[@class='online_stat']") 
    __STORE_BUTTON = (By.XPATH, "//*[@aria-label='Global Menu']/a[@data-tooltip-content='.submenu_Store']") 

    def get_current_players(self):
        raw_text = self.get_text(self.__CURRENT_PLAYERS)  
        cleaned_text = ''.join(filter(str.isdigit, raw_text)) 
        return int(cleaned_text)

    def get_peak_players(self):
        raw_text = self.get_text(self.__PEAK_PLAYERS) 
        cleaned_text = ''.join(filter(str.isdigit, raw_text)) 
        return int(cleaned_text)
    
    def click_store(self):
        self.click_element(self.__STORE_BUTTON)