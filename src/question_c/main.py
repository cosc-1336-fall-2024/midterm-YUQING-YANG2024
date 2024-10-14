#Question c
#3) In main write a program that will continue until users decides to quit, in the loop ask the user for a string and display it's reverse value.

import question_c

def string_reverse_menu():
    print("-----get reverse menu-----\n1-I want to reverse a string!\n2-escape the program")

while True:
    string_reverse_menu()
    option = int(input("Your selection: "))

    if option == 1:
        string = input("Please gave me your string: ")
        result = question_c.reverse_string(string)
        print("Here is your reversed string: ", result)

    elif option == 2:
        print("ESCAPED!")
        exit()

    else:
        print("Invalid")