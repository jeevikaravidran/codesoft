contacts = {}

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Count Contacts")
    print("7. Exit")
    
    choice = input("Enter Your Choice (1-7): ")

    if choice == '1':
        name = input("Enter Contact Name: ")
        if name in contacts:
            print("Contact name {name} already exists.")
        else:
            phone = input("Enter Contact Phone Number: ")
            email = input("Enter Contact Email: ")
            address = input("Enter Contact Address: ")
            contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            print(f"Contact {name} has been added successfully.")


    elif choice == '2':
        name = input("Enter Contact Name to View: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: name")
            print(f"Phone: {contact['phone']}")     
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
        else:
            print(f"Contact {name} not found.")

    elif choice == '3':
        search_name = input("Enter Contact name to search: ").lower()
        found = False

        for name, contact in contacts.items():
            if name.lower() == search_name:
                print(f"Name: {name}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                found = True
        if not found:
         print("Contact not found.")

    elif choice == '4':
        name = input("Enter Name to Update contact: ")
        if name in contacts:
            phone = input("Enter new number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            print(f"Contact {name} has been updated successfully.")
        else:
            print(f"Contact {name} not found.")


    elif choice == '5':
        name = input("Enter Contact Name to Delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully.")
        else:
            print(f"Contact {name} not found.")
    

    elif choice == '6':
        print(f"Total Contacts in your book : {len(contacts)}")

    elif choice == '7':
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")