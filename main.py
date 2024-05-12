from phone_book import PhoneBook

phone_book = PhoneBook()

while True:
    print("\nWelcome to Veronika's Phone Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Print All Contacts")
    print("4. Search Contact")
    print("5. Sort Contacts by Name")
    print("6. Sort Contacts by Phone Number")
    print("7. Remove Duplicate Contacts")
    print("8. Reverse Order of Contacts")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_mobile = input("Enter mobile phone: ")
        phone_home = input("Enter home phone (optional): ")
        work = input("Enter work (optional): ")
        email = input("Enter email (optional): ")
        phone_book.add_contact(first_name, last_name, phone_mobile, phone_home, work, email)

    elif choice == '2':
        first_name = input("Enter first name of contact to delete: ")
        last_name = input("Enter last name of contact to delete: ")
        phone_book.delete_contact(first_name, last_name)

    elif choice == '3':
        phone_book.print_all_contacts()

    elif choice == '4':
        first_name = input("Enter first name of contact to search:")
        last_name = input("Enter last name of contact to search:")
        phone_book.search_contact(first_name, last_name)

    elif choice == '5':
        phone_book.sort_contacts_by_name()

    elif choice == '6':
        phone_book.sort_contacts_by_phone()

    elif choice == '7':
        phone_book.remove_duplicate_contacts()

    elif choice == '8':
        phone_book.reverse_order()

    elif choice == '9':
        break
