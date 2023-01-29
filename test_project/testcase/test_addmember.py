from test_project.pages.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.Main = MainPage()

    def test_add_member(self):


        self.Main.go_to_add_member().add_member().save_member()

    def test_contact_member(self):

        self.Main.go_to_contact().go_to_add_member().add_member()