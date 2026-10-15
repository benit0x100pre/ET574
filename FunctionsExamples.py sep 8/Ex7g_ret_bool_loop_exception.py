# Functions
# Use modulo, % operator to setup conditions
# Use the return statement to generate a return value of a functions

# creating a function
def is_divisible(x, y):
    """function returning a boolean value"""
    return x % y == 0

# creating main() function
def main():
    #implement the exception handling
    try:
        while True: 
            #print("6/12")
            #print("Divisible =", is_divisible(6, 12))
            a, b = int(input("Enter a num: ")), \
        int(input("Enter another number: "))
            if b != 0:
                print(f'{a}/{b}')
                print("Divisible =", is_divisible(a, b))
            else:
                print("ZeroDiisionError! Exit...")
                break
    except:
        print("Exception: Input Error! Exit...")

# calling main() function to initiate the tasks to be performed
main()
    
