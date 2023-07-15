
def main() :
    # say hello
    name = input("Enter your name: ")
    hello(name)
    hello() # prints Hello, world! since no argument is provided

def hello(to="world"): # world is the default value in case to is empty
    print(f"Hello, {to}!")

main()

# without main function or a higher level encompassing function, all the used functions have 
# to be defined higher up in the file before their usage