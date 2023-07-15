#name = input("Enter your name: ")
##name = name.strip() # remove white spaces at both ends of the string
##print(f"Hello, {name}")
#name = name.capitalize() # capitalize capitalizes just the first letter
#print(f"Hello, {name}")
#name = name.title() # capitalizes first letter of each word
#print("printing in Title Case")
#print(f"Hello, {name}")
# we could also use the function chaining to strip and title case at once
# like name = name.strip().title()
name = input("Enter your : ").strip().title()
print(f"Hello, {name}")


first, last = input("Enter your full name: ").split(" ")
print(f"Hello, {first}")