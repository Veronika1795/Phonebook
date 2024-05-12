from contact import Contact


class PhoneBook:
    def __init__(self):
        """Constructor to initialize a PhoneBook object with some sample contacts"""
        self.contacts = []

    def add_contact(self, first_name: str, last_name: str, mobile_phone: str, home_phone: str = '', work: str = '', email: str = ''):
        """Method to add a new contact to the phone book"""
        new_contact = Contact(first_name, last_name, mobile_phone, home_phone, work, email)
        if new_contact not in self.contacts:
            self.contacts.append(new_contact)
        else:
            print("There is same contact. The addition not happened.")

    def delete_contact(self, first_name: str, last_name: str):
        """Method to delete a contact from the phone book based on first name and last name"""
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                return

    def print_all_contacts(self):
        """Method to print all contacts in the phone book."""
        for contact in self.contacts:
            print(f"First Name: {contact.first_name}, Last Name: {contact.last_name}, Mobile: {contact.phone_mobile}, Home: {contact.phone_home}, Work: {contact.work}, Email: {contact.email}")

    def search_contact(self, first_name: str, last_name: str):
        """Method to search for a contact by first name and last name."""
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                print(f"First Name: {contact.first_name}, Last Name: {contact.last_name}, Mobile: {contact.phone_mobile}, Home: {contact.phone_home}, Work: {contact.work}, Email: {contact.email}")

    def sort_contacts_by_name(self):
        """Method to sort contacts in the phone book by name."""
        self.contacts.sort(key=lambda x: (x.first_name, x.last_name))
        print("Phonebook after sort by name:")
        for contact in self.contacts:
            print(f"First Name: {contact.first_name}, Last Name: {contact.last_name}, Mobile: {contact.phone_mobile}, Home: {contact.phone_home}, Work: {contact.work}, Email: {contact.email}")

    def sort_contacts_by_phone(self):
        """Method to sort contacts in the phone book by phone number."""
        self.contacts.sort(key=lambda x: x.phone_mobile, reverse=True)
        print("Phonebook after sort by phone:")
        for contact in self.contacts:
            print(f"First Name: {contact.first_name}, Last Name: {contact.last_name}, Mobile: {contact.phone_mobile}, Home: {contact.phone_home}, Work: {contact.work}, Email: {contact.email}")

    def remove_duplicate_contacts(self):
        """Method to remove duplicate contacts from the phone book."""
        without_duplicates = set(self.contacts)
        self.contacts = list(without_duplicates)

        print("Phonebook after remove duplicates:")
        for contact in self.contacts:
            print(f"First Name: {contact.first_name}, Last Name: {contact.last_name}, Mobile: {contact.phone_mobile}, Home: {contact.phone_home}, Work: {contact.work}, Email: {contact.email}")

    def reverse_order(self):
        """Method to reverse the order of contacts in the phone book."""
        self.contacts.reverse()
        print("Phonebook after reverse order:")
        for contact in self.contacts:
            print(f"First Name: {contact.first_name}, Last Name: {contact.last_name}, Mobile: {contact.phone_mobile}, Home: {contact.phone_home}, Work: {contact.work}, Email: {contact.email}")