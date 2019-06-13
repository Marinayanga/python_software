from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(firstname="upd_test", middlename="upd_iddlename", lastname="upd_last name", nickname="upd_nickname",
                                    title="upd_theme", mobile="upd_89001113322", email="upd_a@a.ru", company="upd_mail",
                                    address="upd_address",
                                    home="upd_89001112233", work="upd_323537", fax="upd_1234567890", email2="upd_alla@man,ru",
                                    email3="upd_dados@ef.ru", homepage="upd_fdfdfdfdf", bday="17", bmonth="June",
                                    byear="2001",
                                    aday="18", amonth="September", ayear="2052", address2="upd_leningradskoe shosse",
                                    phone2="upd_15",
                                    notes="upd_happy birthdae"))
    app.contact.return_to_contact_page()
    app.session.logout()