# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list
    contact = Contact(firstname="test", middlename="middlename", lastname="aha", nickname="nickname",
                                    title="theme", mobile="89001113322", email="a@a.ru", company="mail",
                                    address="address",
                                    home="89001112233", work="323537", fax="1234567890", email2="alla@man,ru",
                                    email3="dados@ef.ru", homepage="fdfdfdfdf", bday="15", bmonth="July",
                                    byear="2000",
                                    aday="17", amonth="April", ayear="2050", address2="leningradskoe shosse",
                                    phone2="15",
                                    notes="happy birthdae")
    app.contact.create_new_contact(contact)
    new_contact = app.contact.get_contact_list
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    app.contact.create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", mobile="",
 #                                       email="", company="", address="", home="", work="",
#                                        fax="", email2="", email3="", homepage="",
#                                        bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",
#                                        address2="", phone2="", notes=""))
#    app.contact.return_to_contact_page()

