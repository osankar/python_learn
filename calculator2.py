# calulator to demonstrate functions that returns value

def main():
    x = int(input("Enter x value: "))
    print("x square is", square(x))

def square(n):
    #return n*n
    return pow(n,2)

main()