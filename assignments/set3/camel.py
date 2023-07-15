"""
Python, by contrast, recommends snake case, whereby words are instead separated by underscores
(_), with all letters in lowercase. For instance, those same variables would be called name, 
first_name, and preferred_first_name, respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable
in camel case and outputs the corresponding name in snake case. Assume that the user’s input
will indeed be in camel case.
"""
camel_case = input("camel case: ")
for c in camel_case:
    if c.islower():
        print (c, end="")
    else:
        low = str(c).lower()
        print(f"_{low}", end="")
print()
