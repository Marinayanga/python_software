from selenium.webdriver.support.select import Select
from model.contact import Contact
import re
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
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # удаляем первый контакт
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)


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

    def modify_contact(self, index, new_contact_data):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # выбираем первый контакт
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # заполянем поля
        self.fill_contact_form(new_contact_data)
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                cells = element.find_elements_by_tag_name("td")
                surname = cells[1].text
                name = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                address=cells[3].text
                all_emails= cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=name,lastname=surname,  all_phones_from_home_page=all_phones,
                                                  address=address, all_emails=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        #middlename = wd.find_element_by_name("middlename").get_attribute("value")
        #nickname = wd.find_element_by_name("nickname").get_attribute("value")
        #title = wd.find_element_by_name("title").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        #company = wd.find_element_by_name("company").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        #fax = wd.find_element_by_name("fax").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        #homepage = wd.find_element_by_name("homepage").get_attribute("value")
        #bday = wd.find_element_by_name("bday").get_attribute("value")
        #bmonth = wd.find_element_by_name("bmonth").get_attribute("value")
        #byear = wd.find_element_by_name("byear").get_attribute("value")
        #aday = wd.find_element_by_name("aday").get_attribute("value")
        #amonth = wd.find_element_by_name("amonth").get_attribute("value")
        #ayear = wd.find_element_by_name("ayear").get_attribute("value")
        #address2 = wd.find_element_by_name("address2").get_attribute("value")
        #notes = wd.find_element_by_name("notes").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, work=work, phone2=phone2, mobile=mobile, email=email,
                       email2=email2, email3=email3, address=address)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # удаляем первый контакт
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        # выбираем первый контакт
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # заполянем поля
        self.fill_contact_form(new_contact_data)
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.contact_cache = None




