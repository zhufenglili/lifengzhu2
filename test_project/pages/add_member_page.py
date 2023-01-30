from time import sleep

from selenium.webdriver.common.by import By

from test_project.pages.basepage import BasePage
from test_project.pages.contact_page import ContactPage


class AddMemberpage(BasePage):
    def add_member(self,username,memberAdd_acctid,memberAdd_phone):

        self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(username)
        self.driver.find_element(By.XPATH,'//*[@id="memberAdd_acctid"]').send_keys(memberAdd_acctid)
        self.driver.find_element(By.XPATH,'//*[@id="memberAdd_phone"]').send_keys(memberAdd_phone)
        return self
    def save_member(self):

        self.driver.find_element(By.CSS_SELECTOR,'[class="qui_btn ww_btn js_btn_save"]').click()
        return ContactPage(self.driver)
    def cancel_member(self):
        pass
