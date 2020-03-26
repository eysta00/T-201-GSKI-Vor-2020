from sortedcollections import *

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactList:
    def __init__(self):
        self.main_map = dict()
        self.name_map = SortedDict()
        self.phone_map = dict()
        self.email_map = dict()