from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage:
    def __init__(self, driver_base=None):
        if driver_base is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver_base
