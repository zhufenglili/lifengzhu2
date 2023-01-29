import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Test_aa():  # 复用浏览器
    def setup(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)

        db=shelve.open('./mysqls/cookies')
        # db['cookie'] = cookeis
        # db.close()
        cookeis =db['cookie']
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookeis:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            # self.driver.add_cookie(cookie)

