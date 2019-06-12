# -*- coding: utf-8 -*-
from contact import Contact
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact()
    app.create_new_contact(Contact(firstname="test", middlename="middlename", lastname="aha", nickname="nickname",
                                    title="theme", mobile="89001113322", email="a@a.ru", company="mail",
                                    address="address",
                                    home="89001112233", work="323537", fax="1234567890", email2="alla@man,ru",
                                    email3="dados@ef.ru", homepage="fdfdfdfdf", bday="15", bmonth="July",
                                    byear="2000",
                                    aday="17", amonth="April", ayear="2050", address2="leningradskoe shosse",
                                    phone2="15",
                                    notes="happy birthdae"))
    app.return_to_contact_page()
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact()
    app.create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", mobile="",
                                        email="", company="", address="", home="", work="",
                                        fax="", email2="", email3="", homepage="",
                                        bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",
                                        address2="", phone2="", notes=""))
    app.return_to_contact_page()
    app.logout()

