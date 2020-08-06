import os
import sys
from prettytable import PrettyTable


# Class Contact
class Contact(object):
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


# Function to write out the contact list
def show_list():
    t = PrettyTable(['Pos', 'Name', 'Surname', 'Number'])
    contacts.sort(reverse=False, key=name)

    for contact in contacts:
        t.add_row([contacts.index(contact) + 1, contact.name,
                   contact.surname, contact.number])

    print(t)


# Function to add a new contact
def add_contact():
    name = input("Name: ")
    surname = input("Surname: ")
    number = input("Phone number: ")
    contacts.append(Contact(name, surname, number))


# Function to remove a contact
def remove_contact():
    if not contacts:
        print("List is empty!")
    else:
        index = input(
            "Enter the position of the contact which is to be removed: ")
        contacts.pop(int(index) - 1)


# For sorting purposes
def name(club):
    return club.name


# Implementing a somewhat of a switch statement
def handling_input():
    print("(a - to add, s - to show, d - to delete, q - to quit)")
    entered = input("Please select desired action: ")
    input_dict[entered]()


# Clearing the console
def clear(): os.system('cls')


# Closing the program
def quit_program(): sys.exit()


# The main function
def main():
    global input_dict, contacts

    clear()

    # Contact list
    contacts = []

    # Possible inputs
    input_dict = {
        'a': add_contact,
        's': show_list,
        'd': remove_contact,
        'q': quit_program,
    }

    # Getting input for a desired action
    while True:
        handling_input()


if __name__ == '__main__':
    main()
