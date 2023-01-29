from time import sleep

from selenium.webdriver.common.by import By

from test_project.pages.basepage import BasePage
from test_project.pages.contact_page import ContactPage


class AddMemberpage(BasePage):
    def add_member(self):
        sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys('你好1')
        self.driver.find_element(By.XPATH,'//*[@id="memberAdd_acctid"]').send_keys('2253')
        self.driver.find_element(By.XPATH,'//*[@id="memberAdd_phone"]').send_keys(13613614531)
        return self
    def save_member(self):

        self.driver.find_element(By.CSS_SELECTOR,'[class="qui_btn ww_btn js_btn_save"]').click()
        return ContactPage(self.driver)
    def cancel_member(self):
        pass
