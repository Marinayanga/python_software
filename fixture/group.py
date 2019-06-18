
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group(self):
        # open group page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group()
        # init group page
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit book create
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group()
        self.select_first_group()
        # войти в режим редактирования
        wd.find_element_by_name("edit").click()
        # вносить изменения
        self.fill_group_form(new_group_data)
        # submit group create
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_group()
        return len(wd.find_elements_by_name("selected[]"))