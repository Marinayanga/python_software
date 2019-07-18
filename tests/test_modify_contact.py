from model.contact import Contact
import random

def test_modify_some_contact(app,db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(
            Contact(firstname="test", middlename="middlename", lastname="aha", nickname="nickname",
                    title="theme", mobile="89001113322", email="a@a.ru", company="mail",
                    address="address",
                    home="89001112233", work="323537", fax="1234567890", email2="alla@man,ru",
                    email3="dados@ef.ru", homepage="fdfdfdfdf", bday="15", bmonth="July",
                    byear="2000",
                    aday="17", amonth="April", ayear="2050", address2="leningradskoe shosse",
                    phone2="15",
                    notes="happy birthdae"))
    def clean(contact):
        return Contact(id = contact.id, firstname = contact.firstname.strip())
    old_contact = db.get_contact_list()
    contact_index = random.choice(range(len(old_contact)))
    contact_to_modify = Contact(firstname="kkkk 333",lastname="fffff 111")
    contact_to_modify.id = old_contact[contact_index].id
    app.contact.modify_contact_by_id(contact_to_modify.id,contact_to_modify)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[contact_index].id = contact_to_modify
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(clean,new_contact), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)