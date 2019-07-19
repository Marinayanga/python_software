from model.contact import Contact
import random

def add_contact_to_group(app,db):

    contact_list=db.get_contact_list
    id = random.choice(contact_list).id
    app.contact.add_contact_to_group(Contact(firstname='kjp'), '%s' % id)