from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url=''
    def __init__(self, driver_base=None):
        if driver_base is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)

            self.driver.implicitly_wait(10)


        else:
            self.driver:WebDriver = driver_base
        if self.base_url !='':
            self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
    def find(self,by,value):
        return self.driver.find_element(by,value)

    def finds(self,by,value):
        return self.driver.find_elements(by,value)
    def wait_for_clikable(self,element):
        return WebDriverWait(self.driver,10).until(ec.element_to_be_clickable(element))

