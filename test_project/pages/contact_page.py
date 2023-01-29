from test_project.pages.basepage import BasePage


class ContactPage(BasePage):
    def go_to_add_member(self):
        from test_project.pages.add_member_page import AddMemberpage

        return AddMemberpage(self.driver)
