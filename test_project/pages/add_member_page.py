from time import sleep

from selenium.webdriver.common.by import By

from test_project.pages.basepage import BasePage
from test_project.pages.contact_page import ContactPage


class AddMemberpage(BasePage):
    _username = (By.XPATH, '//*[@id="username"]')
    _memberAdd_acctid = (By.XPATH, '//*[@id="memberAdd_acctid"]')
    _memberAdd_phone = (By.XPATH, '//*[@id="memberAdd_phone"]')
    _qui_btn =(By.CSS_SELECTOR, '[class="qui_btn ww_btn js_btn_save"]')


    def add_member(self, username, memberAdd_acctid, memberAdd_phone):
        self.find(*self._username).send_keys(username)
        self.find(*self._memberAdd_acctid).send_keys(memberAdd_acctid)
        self.find(*self._memberAdd_phone).send_keys(memberAdd_phone)
        return self

    def save_member(self):
        self.find(*self._qui_btn).click()
        return ContactPage(self.driver)

    def cancel_member(self):
        pass
