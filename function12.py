# Categorizing password as Strong or
# Weak in Python using Regex


import re


# Function to categorize password
def password(v):

    # the password should not be a
    # newline or space
    if v == "\n" or v == " ":
        return "Password cannot be a newline or space!"

    # the password length should be in
    # between 9 and 20
    if 9 <= len(v) <= 20:

        # checks for occurrence of a character
        # three or more times in a row
        if re.search(r'(.)\1\1', v):
            return "Weak Password: Same character repeats three or more times in a row"

        # checks for occurrence of same string
        # pattern( minimum of two character length)
        # repeating
        if re.search(r'(..)(.*?)\1', v):
            return "Weak password: Same string pattern repetition"

        else:
            return "Strong Password!"

    else:
        return "Password length must be 9-20 characters!"

# Main method


def main():

    # Enter the email
    while True:
        passw = input(
            'Enter the Password to check the strength or press X to exit: ')
        if passw == 'X' or passw == 'x':
            break
        print(password(passw))


# Driver Code
if __name__ == '__main__':
    main()
