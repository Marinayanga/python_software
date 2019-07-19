from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(
            Contact(firstname="test", middlename="middlename"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Было нечего", header="удалять", footer="создали тебя"))
    group_id = random.choice(db.get_group_list()).id
    contact_id = random.choice(orm.get_contacts_in_group(Group(id=group_id))).id
    app.contact.delete_contact_from_group(group_id, contact_id)
