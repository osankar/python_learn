
"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate 
for your car, with your choice of letters and numbers instead of random ones. Among the 
requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 
characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, 
AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output
Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in 
the user’s input will be uppercase. Structure your program per the below, wherein is_valid 
returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
You’re welcome to implement additional functions for is_valid to call (e.g., one function per 
requirement).


"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return is_length_ok(s) and has_two_alpha(s) and has_valid_num_alpha(s)

def  is_length_ok(s):
    return len(s) < 7

def has_two_alpha(s):
    for i in range(2):
        if s[i].isalpha():
            continue
        else:
            return False
    return True

def has_valid_num_alpha(s):
    numstarted = False
    for i in range(len(s)):
        if i < 2:
            continue
        if not numstarted and s[i].isalpha():
            return False
        elif s[i].isdigit():
            if s[i] == "0" and not numstarted: 
                return False
            numstarted = True
        elif s[i-1].isalpha():
            continue
        else:
            return False
    return True

main()

