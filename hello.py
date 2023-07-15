# Ask user for the name
name = input("Enter your name: ")
# say hello to user
print("Hello,",name,"!")

"""
This is a 
multiline comment
"""
# override default behavior of print() printing a new line to not do that
print("Hello, ", end="")
print(name)

# in the above case, end is called named parameter. For these parameters we can set the value
# by explicitly setting the value to the parameter with the name. 

#print using the variable with formatted string 
# print(f "String with variables")
print(f"Hello {name}")