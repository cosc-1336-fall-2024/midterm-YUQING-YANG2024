#write functions here, don't add input('') statements here!

#Question c
#1) Create a function named reverse_string that has one parameter named string1 that returns the reverse of the string. 
# MUST USE A WHILE LOOP. DO NOT USE STRING SLICING!!!

def reverse_string(string1):
#get length of the string
    reverse_string1 = ""
    index = len(string1) - 1

#get the index from last to first, combine all the index
    while(index >= 0):
        reverse_string1 += string1[index]
        index -= 1
    return reverse_string1

