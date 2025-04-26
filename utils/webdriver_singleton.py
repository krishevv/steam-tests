from selenium import webdriver

class WebDriverSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebDriverSingleton, cls).__new__(cls)
            cls._instance.driver = None
        return cls._instance

    def get_driver(self):
        if self.driver is None:
            options = webdriver.ChromeOptions()
            options.add_argument("--incognito")  
            options.add_argument("--no-sandbox")  
            options.add_argument("--disable-dev-shm-usage")  
            options.add_argument("--lang=en")  
            options.add_argument("--start-maximized") 
            

            self.driver = webdriver.Chrome(options=options)
            self.driver.maximize_window()
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
