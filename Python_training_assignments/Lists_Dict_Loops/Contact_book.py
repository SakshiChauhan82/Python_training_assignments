print("contact book manger")
# Requirements 
# Display menu continuously until exit.
# User can: 
# 1.Add Contact 
# 2.Search Contact 
# 3.Delete Contact 
# 4.View All Contacts 
# 5.Exit 
# Store contacts in a dictionary or list. 
# Display appropriate messages for invalid operations.
contacts = {}
n=2
while True:
    choice = input("Enter choice  ")
    if choice =="1":
        name = input("Enter name")
        num = int(input("Enter contact"))
        contacts[name] = num
    elif choice == "2":
        name = input("Enter the name you want to search contact of")
        print(contacts.get(name))
    elif choice == "3":
        name = input("Enter the name you want to delete contact of")
        contacts.pop(name, None)
    elif choice == "4":
        print(contacts)
    else:
        print("Invalid choice")
        break