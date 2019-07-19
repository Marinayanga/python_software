import re
from random import randrange
from model.contact import Contact


def test_information_home_page_vs_db(app,db):

    ui_list = app.contact.get_contact_list()
    for contact in ui_list:
        assert contact.firstname == (db.get_contact_by_id(contact.id).firstname).strip()
        assert contact.lastname == (db.get_contact_by_id(contact.id).lastname).strip()
        assert contact.address == (db.get_contact_by_id(contact.id).address).strip()
        assert contact.all_emails == merge_email_like_on_home_page(db.get_contact_by_id(contact.id))
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(db.get_contact_by_id(contact.id))


    # index = randrange(len(old_contact))
    # contact_from_home_page = app.contact.get_contact_list()[index]
    # contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # assert contact_from_home_page.firstname == contact_info_from_edit_page.firstname
    # assert contact_from_home_page.lastname == contact_info_from_edit_page.lastname
    # assert contact_from_home_page.address == contact_info_from_edit_page.address
    # assert contact_from_home_page.all_emails == merge_email_like_on_home_page(contact_info_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2,
                                                                                contact.email3])))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter( lambda x: x is not None, [contact.home,contact.mobile,

                                                                                                         contact.work,contact.phone2]))))