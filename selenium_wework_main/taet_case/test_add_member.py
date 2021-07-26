from selenium_wework_main.page.main import Main


class TestMember:
    def setup(self):
        self.main = Main()
    def test_member(self):
        add_member = self.main.goto_add_member()
        add_member.address()
        assert '大表哥' in add_member.get_member()
