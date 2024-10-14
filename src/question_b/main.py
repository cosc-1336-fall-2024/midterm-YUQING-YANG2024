#Question b
#3) In main write a program that continues until the user decides to quit.
#   Prompt the user for land value and display the assessment value and tax assessed.

import question_b

def property_tax_menu():
    print("-----MENU-----\n1-get_your_property_taxes\n2-exit")

while True:
    property_tax_menu()
    option = int(input("your selection: "))

    if option == 1:
        property_value = int(input("please enter your property value: "))
        result1 = question_b.get_assessment_value(property_value)
        result2 = question_b.get_tax_assessed(result1)

        print("your property's assessment value is: ", result1)
        print("your property's tax assessed is: ", result2)

    elif option == 2:
        print("Exiting the program")
        exit()

    else:
        print("Invalid")
