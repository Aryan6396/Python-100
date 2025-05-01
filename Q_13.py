# Program to convert celsius to fahrenheit
# formula of c to f = {c*(9/5 or 1.8)} + 32
# 0 degree celsius = 32 fahrenheit

#  to fahrenheit
def celsius():
    cel = float(input("Enter the temperature = "))
    fah = ((9/5) *cel)+32
    print(f"The converted value in Fahrenheit is {fah}\u00B0F")

# to celsius
def fahrenheit():
    fah = float(input("Enter the temperature = "))
    cel = (fah - 32) / (9/5)
    print(f"The converted value in celsius is {cel}\u00B0C")

def main():
    while True:
        print("Press 1 for celsius to fahrenheit")
        print("Press 2 for fahrenheit to celsius")
        choice = input("Enter your choice = ")

        match choice:
            case "1":
                return celsius()
            case "2":
                return fahrenheit() 
            case _:
                print("Invalid choice")  


if __name__ == "__main__":
    main()



