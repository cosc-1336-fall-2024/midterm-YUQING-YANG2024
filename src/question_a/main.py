#Question a
#3) Write a program that runs until the user decided to quit, prompt the user for a number, and display the result.

import question_a

def prime_checker():
    print("-----MENU-----\n1-prime number checker\n2-exit")

while True:

    prime_checker()
    option = int(input("your selection: "))

    if option == 1:
        num = int(input("please your number: "))
        result = question_a.value_is_prime(num)

        if result == True:
            print("result: ", num, " is a prime number")

        elif result == False:
            print("result: ", num, "is not a prime number")

    elif option == 2:
        print("Exiting the program")
        exit()

    else:
        print("Invalid")