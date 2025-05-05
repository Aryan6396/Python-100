# Program to make a simple calculator
print("~~~~~~~~~~~~~~~ MINI CALCULATOR ~~~~~~~~~~~~~~~")
num1 = float(input("Enter number : "))
num2 = float(input("Enter number : "))
def add():
    return num1 + num2
def sub():
    return num1 - num2
def mul():
    return num1 * num2
def div():
    return num1 / num2

def main():
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")

    choice = input("Enter your choice : ")

    match choice:
        case "1":
            return add()
        case "2":
            return sub()
        case "3":
            return mul()
        case "4":
            return div()
        case _:
            return("Invalid Input")
        
if __name__ == "__main__":
    print(main())

