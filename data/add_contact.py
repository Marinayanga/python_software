from model.contact import Contact


testdata = [Contact(firstname="Имя 1", middlename="Отчество 1", lastname="Фамилия 1"),
           Contact(firstname="Имя 2", middlename="Отчество 2", lastname="Фамилия 2")]


# testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", mobile="",
#                    email="", company="", address="", home="", work="",fax="", email2="", email3="", homepage="",
#                    bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",address2="", phone2="", notes="")] + \
#           [Contact(firstname=random_string("name", 5), middlename=random_string("middlename",5), lastname=random_string("last",10),
#                    nickname=random_string("nick", 7), title=random_string("title", 5), mobile=random_string("8900",7),
#                    email=random_string("a@a.", 3), company=random_string("company", 7),
#                    address=random_string("Moscow", 7), home=random_string("8900",7), work=random_string("323537", 5),
#                    fax=random_string("12345",5), email2=random_string("a@a.", 3),
#                    email3=random_string("a@a.", 3), homepage=random_string("fdfdfdfdf", 3), bday="15", bmonth="July",
#                    byear=random_string("2",3),aday="17", amonth="April", ayear=random_string("2",3), address2=random_string("Moscow", 7),
#                    phone2=random_string("8900",7),notes=random_string("notes", 7)) for i in range(5)]