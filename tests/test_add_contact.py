# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contact, check_ui):
    contact = json_contact

    def clean(contact):
        return Contact(id = contact.id,  firstname = contact.firstname.strip())
    old_contacts = db.get_contact_list()
    app.contact.create_new_contact(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(clean,new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)






