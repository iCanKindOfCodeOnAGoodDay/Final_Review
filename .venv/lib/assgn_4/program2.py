# Copy and Pasted May 10, 2025, Final Preparations
# Scott Quashen - ISYS 350, SFSU, Assignment 4 - May 2025 - Prof Abdur Sikder

# Employee Management System - Featuring Data Persistence via Reading & Writing Files
# This program loads data into a dictionary then uses commands on that dictionary to manage the employee data
# Exports updated file on program exit

# ------> Input:    Reads data from "employee_data.txt" file to populate "the dictionary" on run
#         Note:     If program can't find "employee_data.txt" it will create it as blank txt file in Project's lib directory
# ------> Output:   On Exit program overwrites "employee_data.txt" with up-to-data data from "the dictionary"

# These (4) Actions can be taken on each employee:

#         (1)-Lookup Employee
#         (2)-Add Employee
#         (3)-Edit Employee
#         (4)-Delete Employee

# In Reflection, I probably would have kept the_employee_dictionary global vs passing it around from main... for readability

def main():
    # each key is an employee ID, and each value is another dictionary with that employee's details
    # think about "the dictionary" as the 'working' version of the txt file
    the_employee_dictionary = {
        # 47800: {
        # "name": "name",
        # "department": "department",
        # "title": "title",
        # },
    }

    # try to read data from file lib/employee_data.txt
    try:
        with open("employee_data.txt", "r") as starting_doc:
            # load data from file into corresponding nested fields of the_employee_dictionary
            for line in starting_doc:
                parts = line.strip().split(",")  # each "parts" is equal to a field value, i.e. one of the parts is name: "name_part"
                if len(parts) == 4:  # make sure we don't cause an index error
                    the_employee_dictionary[int(parts[0])] = {
                        "name": parts[1],
                        "department": parts[2],
                        "title": parts[3],
                    }
                else:
                    print("The included data is corrupt - please inspect txt file data to ensure the proper amount of fields for each employee.")
    # employee_data.txt not in project's lib directory
    except FileNotFoundError:
        print("File not found...\nCreating starting doc...")
        open("employee_data.txt", "w") # create the file since it doesn't exist, blank

    # run the employee management menu loop
    print("Welcome to Employee Management System")
    while True: # present the menu again every time user finishes a command (Lookup, Add, Edit, or Delete)
        print("--------------Choose an option--------------")
        menu_selection = ""
        while True: # deals with invalid menu options
            menu_selection = input("1: Look up employee by ID\n2: Add new employee\n3: Edit employee\n4: Delete employee\n5: Exit\n")
            try:
                numeric_value = int(menu_selection)
                if 0 < numeric_value < 6:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a number between 1 and 5")

        match menu_selection:
            case "1":
                lookup_employee(the_employee_dictionary)
            case "2":
                add_employee(the_employee_dictionary)
            case "3":
                edit_employee(the_employee_dictionary)
            case "4":
                delete_employee(the_employee_dictionary)
            case "5":
                exit(the_employee_dictionary)
                break

# write txt doc
def exit(the_employee_dictionary):
    print('Thank you for using Employee Management System')
    print("Current Employees:\n") # display all employees
    # update the txt document with the current data stored in the the_employee_dictionary
    with open("employee_data.txt", "w") as final_doc:
        for id in the_employee_dictionary:
            final_doc.write(str(id))
            final_doc.write(",")
            final_doc.write(the_employee_dictionary[id]["name"])
            final_doc.write(",")
            final_doc.write(the_employee_dictionary[id]["department"])
            final_doc.write(",")
            final_doc.write(the_employee_dictionary[id]["title"])
            final_doc.write("\n")
            # ready to load live data when program next launched
            print_employee(the_employee_dictionary, id)
            print('\n')

def lookup_employee(the_employee_dictionary):
    id = check_id(the_employee_dictionary)
    print_employee(the_employee_dictionary, id)

def add_employee(the_employee_dictionary):
    id = add_id(the_employee_dictionary) # notice when we get the id here we are using add_id() vs check_id() because in this case we want to ensure the id is not taken vs. the other way around
    name = input("Enter Employee Name: ")
    department = input("Enter Employee Department: ")
    title = input("Enter Employee Title: ")
    # update values in dictionary
    the_employee_dictionary[id] = {
        "name": name,
        "department": department,
        "title": title,
    }
    print_employee(the_employee_dictionary, id)

def edit_employee(the_employee_dictionary):
    id = check_id(the_employee_dictionary)
    print_employee(the_employee_dictionary, id)
    print("What do you want to edit?")
    selection = "default"
    while True:
        selection = input("1: name\n2: department\n3: title\n")
        if selection.isnumeric():
            if 1 <= int(selection) <=3:
                break
        print("Enter only 1, 2, or 3")
    # corresponding updates to dictionary fields
    match selection:
        case "1":
            the_employee_dictionary[id]["name"] = input("Enter New Name: ")
        case "2":
            the_employee_dictionary[id]["department"] = input("Enter New Department: ")
        case "3":
            the_employee_dictionary[id]["title"] = input("Enter New Title: ")
    print_employee(the_employee_dictionary, id) # display the updated employee

def delete_employee(the_employee_dictionary):
    id = check_id(the_employee_dictionary)
    print("The below employee has been deleted")
    print_employee(the_employee_dictionary, id) # printing of this item before deleting is permitted
    the_employee_dictionary.pop(id) # delete

# called after each command so user can see updates 'in real time' vs needing to quit program to view their updated txt doc
def print_employee(the_employee_dictionary, id):
    print("Employee ID:         ", id)
    print("Name:                ", the_employee_dictionary[id]["name"])
    print("Department:          ", the_employee_dictionary[id]["department"])
    print("Title:               ", the_employee_dictionary[id]["title"])

# helper function - for adding employees - makes sure id is not taken
def add_id(the_employee_dictionary):
    while True:
        id = input("Enter Employee ID: ")
        try:
            id = int(id)
            if id in the_employee_dictionary:
                print("This ID is already taken.")
                continue
            return id
        except ValueError:
            print("ID Numbers only")

# helper function - for working with current employees - makes sure id exists
def check_id(the_employee_dictionary):
    while True:
        id = input("Enter Employee ID: ")
        try:
            id = int(id)
            if id not in the_employee_dictionary:
                print("ID not found")
                continue
            return id
        except ValueError:
            print("ID Numbers only")


if __name__ == "__main__":
    main()
