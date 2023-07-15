
x = input("Enter your name: ")
match x:
    case "Harry" |  "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _: # default
        print("Who?")  
"""
name = input("Enter your name: ")
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
   print("Gryffindor")
else:
    print("Who?")

"""
"""
name = input("Enter your name: ")
match name:
    case "Harry": 
         print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who?")  
"""
