def AddNewContact():
    number=int(input("Enter the Number of the person: "))
    name=input("Enter Name of the Person: ")
    email=input("Enter the Email ID of the person: ")
    contactDictionary={"Name":name, "Number":number, "Email":email}
    contactList.append(contactDictionary)

def ViewAllContact():
    contactList.sort(key=lambda item: item['Name'])
    print("-----------------------------------")
    print("Name\tNumber\tEmailID")
    if contactList:
        for contact in contactList:
            print(f"{contact["Name"]}\t{contact["Number"]}\t{contact["Email"]}")
    else:
        print("There are no Contacts")
    
def SearchForContact():
    search=input("Enter the Contact Name You want to search:  ")
    if not contactList:
        print("The contact list is Empty")
        return
    for contact in contactList:
        if search==contact["Name"]:
            print(f"The Name was found the details are {contact}\n")
            break
    else:
        print(f"The Name {search} was not found")

            
def DeleteContact():
    deleteContact=input("Enter the name of the Contact to be deleted: ")
    if not contactList:
        print("The contact list is Empty")
        return
    for contact in contactList:
        if deleteContact==contact["Name"]:
            contactList.remove(contact)
            print("The contact has been suffessfully deleted")
            break
    else:
        print("The contact to be deleted was not found")
        
        
contactList=[]
contactDictionary={}
print("\n-------------------------\nWelcome to Phonebook Program")
while True:
    response=int(input("\n1. Add New Contact\n2. View All Contacts\n3. Search for Contact\n4. Delete Contact\n5. Exit Program\nEnter your choice: "))
    print("\n")
    if response==1:
        AddNewContact()
    elif response==2:
        ViewAllContact()
    elif response==3:
        SearchForContact()
    elif response==4:
        DeleteContact()
    elif response==5:
        break
    else:
        print("Invalid option Enter your choice again")