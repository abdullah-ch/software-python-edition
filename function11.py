# Python program to validate an Email

# import re module

# re module provides support
# for regular expressions
import re

# Make a regular expression
# for validating an Email
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

# Define a function for
# for validating an Email


def check(email):

    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")


# Driver Code
if __name__ == '__main__':

    # Enter the email
    while True:
        email = input('Enter the Email: or press X to exit: ')
        if email == 'X' or email == 'x':
            break
        check(email)

    # calling run function
