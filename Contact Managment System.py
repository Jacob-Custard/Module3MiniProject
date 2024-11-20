# Project Requirements
#Your task is to develop a Contact Management System with the following features:
# 1. Create a user-friendly command-line interface (CLI) for the Contact Management System. Display a welcoming message and provide a menu with the following options:
#add new contact, edit an existing contact, delete a contact, search for a contact, display all contacts, export contacts to a text file, import contacts from a text file (bonus), quit
# 2. Use nested dictionaries as the main data structure for storing contact information. Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
#Store contact details within the inner dictionary, including: name, phone number, email address, additional info
# 3. Implement the menu actions provided in part 1.
# 4. Utilize input() to enable users to select menu options and provide contact details. Implement input validation using regular expressions (regex) to ensure correct formatting of contact information. 
# 5. Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.
# 6. Create a GitHub repository for your project. Create a clean and interactive README.md file in your GitHub repository. Include clear instructions on how to run the application and explanations of its features.

def add_contact(directory):                                                                                                                                                                                                                                 #defining a function to add a contact
    contact = input("Please enter the phone number of the contact you wish to add: ")                                                                                                                                                                       #getting the phone number of the contact to be added
    if contact in directory:                                                                                                                                                                                                                                #if statement checking to see if the contact already exists
        print("This contact already exists.")                                                                                                                                                                                                               #print statement telling the user the cotnact already exists

    else:                                                                                                                                                                                                                                                   #else statement to carry out the adding process for when the cotnact doesnt already exist
        print("\nPlease enter N/A for any information you don't have or don't wish to provide.\n")                                                                                                                                                          #print statement, letting the user know not leave anything blank, to help with error handling
        name = input("Please enter the new contact's name: ")                                                                                                                                                                                               #input statements getting the name, address, and email of the new contact
        address = input("Please enter the new contact's street address: ")
        email = input("Please enter new contact's email address: ")  
        directory[contact] = {"Name": name, "Phone Number": contact, "Address": address, "Email": email}                                                                                                                                                    #adding the contact to the dictionary
        print(f"\n{contact} and associated info has been added to contacts.")                                                                                                                                                                               #print statement telling the user the cotnact has been added

def edit_contact(directory):                                                                                                                                                                                                                                #defining a function to edit the cotnact list
    print("This is the current list of contacts.\n")                                                                                                                                                                                                        #print statement giving the current list of contacts that can be edited
    for contact in directory:
        print(f"{directory[contact]["Name"]}: {contact}") 

    contact_choice = input("Please enter the contact you wish to edit (XXX-XXX-XXXX): ")                                                                                                                                                                   #input statement asking the user which contact they'd like to edit
    edit_choice = input("Which catagory would you like to edit (Name, Address, Email): ").lower()                                                                                                                                                          #input getting which catagory of a cotnact the user would like to edit/update
    
    if edit_choice == "name":                                                                                                                                                                                                                              #series of if elif statements determining which catagory the user selected to edit
        new_name = input("Please enter the new name for the contact: ")                                                                                                                                                                                    #input statement asking the user for the new name of the contact
        try:                                                                                                                                                                                                                                               #try block for error handling 
            directory[contact_choice]["Name"] = new_name                                                                                                                                                                                                   #updating the contact with the new information
            print(f"\nName for has been changed to {new_name}")                                                                                                                                                                                            #print statement telling the user the name has been updated 
        except KeyError:                                                                                                                                                                                                                                   #except block to handle KeyError and let the user know their input was not recognized
            print("\nContact not recognized, please enter contact in the format of XXX-XXX-XXXX\n")    
    
    elif edit_choice == "address":                                                                                                                                                                                                                         #elif set up exactly the same as the previous if statement, but for when the user wants to edit the address of the contact
        new_address = input("Please enter the new address for the contact: ")
        try:
            directory[contact_choice]["Address"] = new_address
            print(f"Address has been changed to {new_address}.")   
        except KeyError:
            print("\nContact not recognized, please enter contact in the format of XXX-XXX-XXXX\n")      

    elif edit_choice == "email":                                                                                                                                                                                                                           #elif statement for the user to edit the email of the cotnact.
        new_email = input("Please enter the new email for the contact: ")
        try:
            directory[contact_choice]["Email"] = new_email
            print(f"The email has been changed to {new_email}.")
        except KeyError:
            print("\nContact not recognized, please enter contact in the format of XXX-XXX-XXXX\n")  

    else:                                                                                                                                                                                                                                                 #else statement telling the user their input was not recognized
        print("Your input was not recognized.")

def delete_contact(directory):                                                                                                                                                                                                                              #defining a function to delet a contact
    print("This is the currrent list of cotnacts.\n")                                                                                                                                                                                                       #print statemet and for loop giving the user the current list of cotnacts
    for contact in directory:
        print(f"{directory[contact]["Name"]}: {contact}")

    user_choice = input("Which contact would you like to delete (XXX-XXX-XXXX): ")                                                                                                                                                                          #input asking the user which contact they'd like to delete
    try:                                                                                                                                                                                                                                                    #try block for error handling
        del directory[user_choice]                                                                                                                                                                                                                          #deleting the selected contact
        print(f"\nThe contact {user_choice} has been deleted.\n")                                                                                                                                                                                           #print statement letting the user know the cotnact has been deleted
    except KeyError:                                                                                                                                                                                                                                        #except block for KeyError and print statement letting the user know their input was not recognized
        print("\nContact not recognized. Please make sure to enter contact in the XXX-XXX-XXXX fomrat.\n")

def search_for_contact(directory):                                                                                                                                                                                                                          #defining a function to search for a contact
    user_choice = input("Do you want to search for a name, phone number, address, or email: ").lower()                                                                                                                                                      #input asking which catagorey theyd like to use in their search
    contact_found = False                                                                                                                                                                                                                                   #setting up a boolean to be used later in the funciton

    if user_choice == "name":                                                                                                                                                                                                                               #series of if elif statements that search the contacts based off the user's chosen catagory
        name = input("\nEnter the name you want to search for: ").title()                                                                                                                                                                                   #input statement getting what the user is searching for
        for contact in directory:                                                                                                                                                                                                                           #for loop to cycle through the contacts dictonary
            if directory[contact]["Name"] == name:                                                                                                                                                                                                          #ascertaining if the user input is in the dictonary
                contact_found = True                                                                                                                                                                                                                        #changing the boolean because the input was found 
                print(f"Contact found\nContact info: {directory[contact]["Name"]} - {directory[contact]["Phone Number"]} - {directory[contact]["Address"]} - {directory[contact]["Email"]}")                                                                #letting the user know the contact was found and printing off the full contact info

    elif user_choice == "phone number":                                                                                                                                                                                                                                                                                                                     
        number = input("\nEnter the phone number you want to search for (XXX-XXX-XXXX): ").strip()
        for contact in directory:
            if contact == number:
                contact_found = True
                print(f"Contact found\nContact info: {directory[contact]["Name"]} - {directory[contact]["Phone Number"]} - {directory[contact]["Address"]} - {directory[contact]["Email"]}")
        
    elif user_choice == "address":
        address = input("\nEnter the address you want to search for: ").strip()
        for contact in directory:
            if directory[contact]["Address"] == address:
                contact_found = True
                print(f"Contact found\nContact info: {directory[contact]["Name"]} - {directory[contact]["Phone Number"]} - {directory[contact]["Address"]} - {directory[contact]["Email"]}")
        
    elif user_choice == "email":
        email = input("\nEnter the email you want to search for: ").strip()
        for contact in directory:
            if directory[contact]["Email"] == email:
                contact_found = True
                print(f"Contact found\nContact info: {directory[contact]["Name"]} - {directory[contact]["Phone Number"]} - {directory[contact]["Address"]} - {directory[contact]["Email"]}")
    else:                                                                                                                                                                                                                                                 #else statement letting the user know their input was not recognized
        print("Search parameter not recognized. Only one of these [name, phone number, address, email] will be recognized.")

    if not contact_found:                                                                                                                                                                                                                                 #if block determining whether or not the boolean is false
        print ("\nSearch inquiry not found.")                                                                                                                                                                                                             #if the boolean is false print statement telling the user their search inquiry was not found

def display_contacts(directory):                                                                                                                                                                                                                            #defining a function to display all contacts
    for contact in directory:                                                                                                                                                                                                                               #for loop to cycle through the directory
        print(f"{directory[contact]["Name"]}: {directory[contact]["Phone Number"]} - {directory[contact]["Address"]} - {directory[contact]["Email"]}")                                                                                                      #print statement that displays the contacts in a formatted manner for the user

def export_contacts(filename, directory):                                                                                                                                                                                                                   #defining a funciton to export contacts to a text file
    with open(filename, 'w') as file:                                                                                                                                                                                                                       #opening the file/creating the file if it doesnt exist
        for contact in directory:                                                                                                                                                                                                                           #for loop to cycle through the dictionary
            file.write(f"{directory[contact]["Name"]}, {directory[contact]["Phone Number"]}, {directory[contact]["Address"]}, {directory[contact]["Email"]}\n")                                                                                             #writing each contact to the file in a formatted manner
            print("Files have been exported.")

def import_contacts(filename):                                                                                                                                                                                                                              #defining a function to import contacts from a text file
    try:                                                                                                                                                                                                                                                    #try block for error handling 
        with open(filename, 'r') as file:                                                                                                                                                                                                                   #opening the file to read
            for line in file:                                                                                                                                                                                                                               #for loop to cycle through each line in the file
                name, phone, address, email = line.strip().split(',')                                                                                                                                                                                       #splitting the info in each line into individual variables
                contacts.update({phone: {"Name": name, "Phone Number": phone, "Address": address, "Email": email }})                                                                                                                                        #updating the contacts dictionary with the new contacts     
    
    except FileNotFoundError:                                                                                                                                                                                                                               #except block for FileNotFoundError and print statement letting the user know the file couldnt be accessed
        print("file not found")                            

contacts = {"405-663-2269": {"Name": "John Jones", "Phone Number": "405-663-2269", "Address": "8313 NW 100th St", "Email": "johnjones555@gmail.com"}}                                                                                                       #establishing the contacts dictionary with a contaxct already in it

while True:                                                                                                                                                                                                                                                 #while loop to cycle through functions until the user decides to exit the program
    print("\nWelcome to the Contact Management Application!")                                                                                                                                                                                               #welcome statement
    print("\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit")                                    #print statement listing the options for the user
    choice = input("What would you like to do?(1-8): ")                                                                                                                                                                                                     #input to gain the user's choice

    if choice == "1":                                                                                                                                                                                                                                       #series of if elif statements to carry out the chosen function
        add_contact(contacts)

    elif choice == "2":
        edit_contact(contacts)
    
    elif choice == "3": 
        delete_contact(contacts)   

    elif choice == "4":
        search_for_contact(contacts)   

    elif choice == "5":     
        display_contacts(contacts)

    elif choice =="6":
        export_contacts("contacts export.txt", contacts)   

    elif choice == "7":
        user_file = input("Enter the relative path of the file you want to import from: ")                                                                                                                                                                 #input to get the file the user wishes to import contacts from
        import_contacts(user_file)   

    elif choice == "8":
        print("Thank you for using the Contact Managment Appliction, goodbye!")                                                                                                                                                                            #goodbye statement
        break                                                                                                                                                                                                                                              #break to end the while loop

    else:                                                                                                                                                                                                                                                  #else statement letting the user know their input was not recognized
        print("Input not recognized.") 


