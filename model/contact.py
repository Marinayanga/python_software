from sys import maxsize


class Contact:

    def __init__(self, id=None,firstname=None, middlename=None, lastname=None, nickname=None, title=None, mobile=None, email=None, company=None,
                 address=None, home=None, work=None,
                 fax=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None,
                 address2=None, phone2=None, notes=None, all_phones_from_home_page=None, all_emails=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.mobile = mobile
        self.email = email
        self.company = company
        self.address = address
        self.home = home
        self.work = work
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and \
               self.firstname == other.firstname

    def id_or_max (self):
       if self.id:
           return int(self.id)
       else:
           return maxsize
