"""
x = input("Enter x: ")
y = input("Enter y: ")
z = x+y
print(z) # prints z value as the concatenation of x and y if x=1 and y=2, then z = 12
"""
# Integer
print("Integer Sum")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print("The sum is", (x+y))

# float
print("float sum")
x = float(input("Enter x: "))
y = float(input("Enter y: "))
# print("The sum is", (x+y))
# cprint("The sum rounded to nearest integer", round(x+y)) 
# round takes a second argument that can be used prescribe the number of decimal places. 

#format to us format
z=x+y
print(f"{z:,}") #prints 1000 like 1,000

