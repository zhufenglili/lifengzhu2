from selenium.webdriver.common.by import By

from test_project.pages.basepage import BasePage



class ContactPage(BasePage):
    def go_to_add_member(self):
        from test_project.pages.add_member_page import AddMemberpage

        return AddMemberpage(self.driver)
    def get_member_list(self):
       ele =self.driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
       print(ele)

       return [i.text for i in ele]