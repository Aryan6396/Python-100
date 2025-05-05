# Program to find factorial using recursion

def fact(n):
    if n <= 1:
        return n
    else:
        return n*fact(n-1)
    
n = int(input("Enter a number here : "))
print("The factorial of all natural numbers upto",n,"is",fact(n))