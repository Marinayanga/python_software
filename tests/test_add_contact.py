# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.add_contact import constant as testdata


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


