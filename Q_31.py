# Program to convert decimal to binary using recursion
n = int(input("enter a number : "))
def convertbinary(n):
    if n>1:
        convertbinary(n//2)
    print(n%2,end="")

print("The binary conversion of number",n,"is : ")
convertbinary(n)
