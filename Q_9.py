# Program to find largest no among three numbers

num1 = float(input("Enter a number = "))
num2 = float(input("Enter a number = "))
num3 = float(input("Enter a number = "))

if (num1 > num2) and (num1 > num3):
    print(num1, "is largest number among three numbers")
elif (num2 > num3) and (num2 > num1):
    print(num2, "is largest number among three numbers")
else:
    print(num3, "is largest number among three numbers")