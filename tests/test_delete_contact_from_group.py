from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(
            Contact(firstname="test", middlename="middlename"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Было нечего", header="удалять", footer="создали тебя"))
    if len(db.get_groups_with_contacts())==0:
        contact_id = random.choice(db.get_contact_list()).id
        group_id = random.choice(db.get_group_list()).id
        app.contact.add_contact_to_group(contact_id, group_id)
    group_id = random.choice(db.get_groups_with_contacts()).id
    contact_id = random.choice(orm.get_contacts_in_group(Group(id=group_id))).id
    app.contact.delete_contact_from_group(group_id)
    assert db.get_contact_by_id(contact_id) not in orm.get_contacts_in_group(Group(id=group_id))

