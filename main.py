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
def write_list():
    pass


# Function to add a new contact
def add_contact():
    name = input("Name: ")
    surname = input("Surname: ")
    number = input("Phone number: ")
    contacts.append(Contact(name, surname, number))


# Function to remove a contact
def remove_contact():
    pass

# Implementing a somewhat of a switch statement


def handling_input(argument):
    return input_dict.get(argument, clear())


def clear(): os.system('cls')


def quit_program(): sys.exit()


def main():
    global input_dict, contacts

    # Possible inputs
    input_dict = {
        'a': add_contact,
        'w': write_list,
        'd': remove_contact,
        'q': quit_program,
    }

    # Contact list
    contacts = []

    # Getting input for a desired action
    run = True

    while run:
        print("(a - to add, w - to write, d - to delete, q - to quit)")
        entered = input("Please select desired action: ")
        handling_input(entered)


if __name__ == '__main__':
    main()
