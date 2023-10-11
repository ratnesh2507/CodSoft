import sys
class Calculator:
    def add(self, a, b):
        print("Sum:", a+b)

    def subtract(self, a, b):
        print("Difference:", a-b)

    def multiply(self, a, b):
        print("Product:", a*b)

    def divide(self, a, b):
        print("Quotient:", a/b)

ob = Calculator()
while True:
    print("\n----Calculator Application----")
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 5 to Exit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        ob.add(a,b)

    elif choice == 2:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        ob.subtract(a,b)

    elif choice == 3:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        ob.multiply(a,b)

    elif choice == 4:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        ob.divide(a,b)

    elif choice == 5:
        sys.exit(0)
        
    else:
        print("Enter valid choice!!")
