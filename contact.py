class Contact:
    def __init__(self, first_name, last_name, phone_mobile, phone_home='', work='', email=''):
        """Constructor to initialize a Contact object with provided details"""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_mobile = phone_mobile
        self.phone_home = phone_home
        self.work = work
        self.email = email

    def __eq__(self, other):
        """Override the equality operator to compare Contact objects"""
        return self.first_name == other.first_name and \
               self.last_name == other.last_name and \
               self.phone_mobile == other.phone_mobile

    def __hash__(self):
        """ Override the hash function to enable hashing of Contact objects"""
        return hash((self.first_name, self.last_name, self.phone_mobile))

