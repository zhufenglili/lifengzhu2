from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        sleep(3)

    def teardown(self):
        self.driver.quit()

    def test_a(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id="s-top-loginbtn"]').click()
        sleep(3)
        dowindow_dangqian=self.driver.current_window_handle
        self.driver.find_element(By.CSS_SELECTOR, '[id="TANGRAM__PSP_11__regLink"]').click()
        sleep(5)
        suoyou= self.driver.window_handles
        self.driver.switch_to.window(self.driver.window_handles[0])#切换窗口并把定义的所有窗口中获取切换的窗口
        sleep(5)
        print(dowindow_dangqian)
        print(suoyou)

