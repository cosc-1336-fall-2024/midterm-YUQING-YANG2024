#write functions here, don't add input('') statements here!

#Question a
#1) Write a function is_prime that returns True if a number is prime False otherwise.

#def test_config():
#    return True

def value_is_prime(num):
    #the input number should be integer and larger than 1,

    if num > 1:
        #num is divisible by 2 or any number less than it, it is not a prime
        for i in range(2, num):
            if num % i == 0:
                return False
                #print("result: ", num, " is not a prime number")

            else:
                return True
                #print("result: ", num, " is a prime number")

    else:
        print("It is not a valid number")