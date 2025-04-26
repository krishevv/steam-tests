import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BestSellersPage(BasePage):

    __MORE_TOP_SELLERS_BUTTON = (By.XPATH, "//button[contains(text(),'Browse')]")
    __LINUX_CHECKBOX = (By.XPATH, "//span[contains(@data-loc,'Linux')]")
    __NARROW_BY_NUMBER_OF_PLAYERS = (By.XPATH,"//*[contains(text(), 'Narrow by number of players')]")
    __LAN_COOP_CHECKBOX = (By.XPATH, "//span[contains(@data-loc,'LAN') and contains(@data-loc,'Co-op')]")
    __ACTION_CHECKBOX = (By.XPATH, "//span[@data-loc='Action'][1]")
    __CONTROL_COUNT = (By.XPATH, "//*[@data-loc='Action']//span[@class='tab_filter_control_count']")
    __RESULTS_COUNT = (By.XPATH, "//*[@class='search_results_count']")

    __FIRST_GAME = (By.XPATH, "//*[@id='search_resultsRows']/a[1]")
    __FIRST_GAME_TITLE = (By.XPATH, "//*[@id='search_resultsRows']/a[1]//*[@class='title']")
    __FIRST_GAME_PRICE = (By.XPATH, "//*[@id='search_resultsRows']/a[1]//*[@class='discount_final_price']")
    __FIRST_GAME_RELEASE_DATE = (By.XPATH, "//*[@id='search_resultsRows']/a[1]//*[contains(@class,'search_released')]")

    def click_more_top_sellers(self):
        element = self.find_element(self.__MORE_TOP_SELLERS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element) 
        element.click()

    def select_filters(self):
        
        self.click_element(self.__LINUX_CHECKBOX)
        
        element = self.find_element(self.__NARROW_BY_NUMBER_OF_PLAYERS)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element) 
        element.click()
    
        time.sleep(1)
        checkbox_lan = self.find_element(self.__LAN_COOP_CHECKBOX)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_lan)
        checkbox_lan.click()
        time.sleep(4)
        control_count_text = self.get_text(self.__CONTROL_COUNT)
        self.click_element(self.__ACTION_CHECKBOX)
        time.sleep(1)
        results_count_text = self.get_text(self.__RESULTS_COUNT)
        
        return int(control_count_text), int(results_count_text[:2]) 

    def is_checkbox_selected(self, locator):
        checkbox = self.find_element(locator)
        return 'checked' in checkbox.get_attribute('class')

    def is_linux_checkbox_selected(self):
        return self.is_checkbox_selected(self.__LINUX_CHECKBOX)

    def is_lan_coop_checkbox_selected(self):
        return self.is_checkbox_selected(self.__LAN_COOP_CHECKBOX)

    def is_action_checkbox_selected(self):
        return self.is_checkbox_selected(self.__ACTION_CHECKBOX)
    
  
          
    def get_first_game_info(self):
    
        title = self.get_text(self.__FIRST_GAME_TITLE)
        price = self.get_text(self.__FIRST_GAME_PRICE)
        release_date = self.get_text(self.__FIRST_GAME_RELEASE_DATE)
        return title, price, release_date

    def open_first_game(self):
        
        self.click_element(self.__FIRST_GAME)
