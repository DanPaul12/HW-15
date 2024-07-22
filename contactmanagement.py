
contacts = {
    8052174796 : {"Name": "Dan Schechter", "email": "danandrum@gmail.com"},
    8586924163 : {"Name": "Alyssa Virker", "email": "alyssa.c.virker@gmail.com"}
}

def add_contact(contacts):
    phone_number = int(input("What is contact's phone number?: "))
    name = input("What is contact's name?: ")
    email = input("What is contact's email?: ")
    contacts[phone_number] = {"Name": [name], "email": [email]}
    print(contacts)

def edit_contact(contacts):
    num = int(input("What is the phone number of the contact you'd like to edit?: "))
    for contact, _ in contacts.items():
        if num == contact:
            new_name = input("What is contact's name?: ")
            new_email = input("What is contact's email?: ")
            contacts[contact]= {"Name": [new_name], "email": [new_email]}
            print(contacts)

def delete_contacts(contacts):
    num = int(input("What is the phone number of the contact you'd like to delete?: "))
    del contacts[num]
    print(contacts)

def search_contacts(contacts):
    num = int(input("What is the number of the contact?:"))
    for contact, _ in contacts.items():
        if num == contact:
            print(contacts[contact])
        else:
            print("Contact not found")

while True:
    command = int(input("Welcome to the Contact Management System! \nMenu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file *BONUS*\n8. Quit\nSelect a number 1-8: "))
    if command == 1:
        add_contact(contacts)
    elif command == 2:
        edit_contact(contacts)
    elif command == 3:
        delete_contacts(contacts)
    elif command == 4:
        search_contacts(contacts)
    elif command == 5:
        print(contacts)
    elif command == 6:
        pass
    elif command == 7:
        pass
    elif command == 8:
        break
    else:
        print("Invalid command")