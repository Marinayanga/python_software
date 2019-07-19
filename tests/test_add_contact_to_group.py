from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMfixture

db = ORMfixture(host='127.0.0.1', name = 'addressbook', user = 'root', password='')

def test_add_contact_to_group(app,db):

    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(
            Contact(firstname="test", middlename="middlename"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Было нечего", header="удалять", footer="создали тебя"))
    contact_list=db.get_contact_list()
    group_list = db.get_group_list()
    contact_id = random.choice(contact_list).id
    group_id = random.choice(group_list).id
    app.contact.add_contact_to_group(contact_id, group_id)