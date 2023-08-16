#حامد شهاب الصبري


def view(contacts):
    print("Contacts:")
    for name, number in contacts.items():
        print(f"\nName:{name} \nNumber:{number} ")

def add(contact,name,number):
    contacts[name] = number
    print(f"{name} added to your contacts")

def update(contact, name, number):
    if name in contacts:
        contacts[name] = number
        print("Updated successfully!")
    else:
        print(f"{name} was not found in your contacts")

def delete(contacts,name):
    if name in contacts:
        del contacts[name]
        print("{name} deleted successfully!")
    else:
        print(f"{name} was not found in your contacts")
        

    
    
    
contacts = {}

while True:
    print("\n1-View Contacts \n2-Add Contact \n3-Update Contact \n4-Delete Contact")
    
    choice = input("Enter your choice:")
    
    if choice == '1':
        view(contacts)
    elif choice == '2':
        name = input("Enter name:")
        number = input("Enter number:")
        add(contacts, name, number)
    elif choice == '3':
        name = input("Enter the name:")
        number = input("Enter the updated number:")
        update(contacts, name , number)
    elif choice == '4':
        name = input("Enter the name:")
        delete(contacts, name)
    else:
        print("Invalid choice.")
        
    
    
    
    