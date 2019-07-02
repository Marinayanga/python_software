# -*- coding: utf-8 -*-
from model.contact import Contact
import string
import random
import pytest


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", mobile="",
                   email="", company="", address="", home="", work="",fax="", email2="", email3="", homepage="",
                   bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",address2="", phone2="", notes="")] + \
          [Contact(firstname=random_string("name", 5), middlename=random_string("middlename",5), lastname=random_string("last",10),
                   nickname=random_string("nick", 7), title=random_string("title", 5), mobile=random_string("8900",7),
                   email=random_string("a@a.", 3), company=random_string("company", 7),
                   address=random_string("Moscow", 7), home=random_string("8900",7), work=random_string("323537", 5),
                   fax=random_string("12345",5), email2=random_string("a@a.", 3),
                   email3=random_string("a@a.", 3), homepage=random_string("fdfdfdfdf", 3), bday="15", bmonth="July",
                   byear=random_string("2",3),aday="17", amonth="April", ayear=random_string("2",3), address2=random_string("Moscow", 7),
                   phone2=random_string("8900",7),notes=random_string("notes", 7)) for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contact = app.contact.get_contact_list()
#    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", mobile="",
#                                       email="", company="", address="", home="", work="",
#                                        fax="", email2="", email3="", homepage="",
#                                        bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",
#                                        address2="", phone2="", notes="")
#    app.contact.create_new_contact(contact)
#    new_contact = app.contact.get_contact_list()
#    assert len(old_contact) + 1 == len(new_contact)
#    old_contact.append(contact)
#    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


