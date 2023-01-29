from time import sleep

from selenium import webdriver


class Test_sclltop():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_scl(self):
        self.driver.execute_script('document.documentElement.scrollTop=100000')
        sleep(5)