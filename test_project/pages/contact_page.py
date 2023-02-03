from selenium.webdriver.common.by import By

from test_project.pages.basepage import BasePage


class ContactPage(BasePage):
    _member_colRight_memberTable = (By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')

    def go_to_add_member(self):
        from test_project.pages.add_member_page import AddMemberpage

        return AddMemberpage(self.driver)

    def get_member_list(self):
        ele = self.finds(*self._member_colRight_memberTable)

        print(ele)

        return [i.text for i in ele]
