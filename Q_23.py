# Program to find HCF or GCD
x = int(input("Enter a number : "))
y = int(input("Enter a number : "))
HCF = 0
def calcHCF(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if (x % i == 0) and (y % i == 0):
            HCF = i
    return HCF

print("The HCF of given two numbers is :",calcHCF(x,y))
