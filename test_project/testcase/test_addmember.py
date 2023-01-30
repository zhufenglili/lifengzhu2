from test_project.pages.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.Main = MainPage()

    def test_add_member(self):
        list_member = self.Main.go_to_add_member().add_member('郑爽',28,13613415987).save_member().get_member_list()
        assert '郑爽' in list_member

    def test_contact_member(self):
        self.Main.go_to_contact().go_to_add_member().add_member()

    def teardown(self):
        self.Main.driver.quit()
