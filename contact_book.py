class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f'Contact {name} added successfully.')

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts):
                print(f'{i + 1}. {contact.name} - {contact.phone}')

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                self.display_contact(contact)

    def update_contact(self, index, name, phone, email, address):
        if 0 <= index < len(self.contacts):
            self.contacts[index].name = name
            self.contacts[index].phone = phone
            self.contacts[index].email = email
            self.contacts[index].address = address
            print(f'Contact {name} updated successfully.')
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            removed_contact = self.contacts.pop(index)
            print(f'Contact {removed_contact.name} deleted successfully.')
        else:
            print("Invalid contact index.")

    def display_contact(self, contact):
        print(f'Name: {contact.name}')
        print(f'Phone: {contact.phone}')
        print(f'Email: {contact.email}')
        print(f'Address: {contact.address}')

def main():
    manager = ContactManager()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == '4':
            index = int(input("Enter the contact number to update: ")) - 1
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            manager.update_contact(index, name, phone, email, address)
        elif choice == '5':
            index = int(input("Enter the contact number to delete: ")) - 1
            manager.delete_contact(index)
        elif choice == '6':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
