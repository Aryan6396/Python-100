# Program to find sum of natural numbers using recursion

def NNS(n):
    if n <= 1:
        return n
    else:
        return (n)+NNS(n-1)
    
n = int(input("Enter a number here : "))

if n <= 0:
    print("please enter a positive number")
else:
    print("The sum of all natural numbers upto",n,"is",NNS(n))