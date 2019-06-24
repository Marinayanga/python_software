from selenium.webdriver.support.select import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/") and len(wd.find_elements_by_name("MainForm")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create_new_contact(self, contact):
        # create new contact
        wd = self.app.wd
        self.open_home_page()
        # нажать на кнопку добавления нового контакта
        self.add_new_contact()
        #заполнить поля формы
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_contact_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # выбираем первый контакт
        wd.find_element_by_name("selected[]").click()
        # удаляем первый контакт
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.select_field_value("bday",contact.bday)
        self.select_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.select_field_value("aday", contact.aday)
        self.select_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def modify_contact(self, new_contact_data):
        wd = self.app.wd
        # выбираем первый контакт
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # заполянем поля
        self.fill_contact_form(new_contact_data)
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            cells = element.find_elements_by_tag_name("td")
            surname = cells[1].text
            name = cells[2].text
            id = element.find_element_by_name("selected[]").get_attribute("id")
            contacts.append(Contact(lastname=surname, firstname=name, id=id))
        return contacts

