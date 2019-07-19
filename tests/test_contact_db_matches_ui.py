from model.contact import Contact


def test_information_on_home_page(app,db):
    db_list= db.get_contact_list()
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(),lastname=contact.lastname.strip(), address=contact.address.strip() )
    sorted(ui_list, key=Contact.id_or_max) == sorted(map(clean, db_list), key=Contact.id_or_max)