print("\n----------CONTACT BOOK----------")

def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact Added Successfully")

def view_contacts(contacts):
    if len(contacts) == 0:
        print("No Contacts Found")
    else:
        print("\nCONTACT LIST")
        for i, contact in enumerate(contacts):
            print(f"{i+1}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    search = input("Enter Name or Phone Number: ")

    for contact in contacts:
        if contact["name"] == search or contact["phone"] == search:
            print("\nContact Found")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            return
        
    print("Contact Not Found")

def update_contact(contacts):
    name = input("Enter Contact Name to Update: ")

    for contact in contacts:
        if contact["name"] == name:
            print("\nEnter New Details")

            contact["phone"] = input("New Phone Number: ")
            contact["email"] = input("New Email: ")
            contact["address"] = input("New Address: ")
            print("Contact Updated Successfully!")
            return

    print("Contact Not Found")

def delete_contact(contacts):
    name = input("Enter Contact Name to Delete: ")

    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Contact Deleted Successfully")
            return

    print("Contact Not Found")

contacts = []

while True:
    print("\nCONTACT BOOK MENU\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")

    choice = input("Enter Your Choice: ")
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        update_contact(contacts)
    elif choice == "5":
        delete_contact(contacts)
    elif choice == "6":
        print("Thank You For Using Contact Book")
        break
    else:
        print("Invalid Choice")