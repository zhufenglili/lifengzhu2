from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


from test_project.pages.add_member_page import AddMemberpage
from test_project.pages.basepage import BasePage
from test_project.pages.contact_page import ContactPage


class MainPage(BasePage):
    def go_to_contact(self):

        self.driver.find_element(By.CSS_SELECTOR,'[id="menu_contacts"]').click()
        return ContactPage(self.driver)

    def go_to_add_member(self):

        self.driver.find_element(By.CSS_SELECTOR,'[node-type="addmember"]').click()
        sleep(3)
        return AddMemberpage(self.driver)

