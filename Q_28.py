# Program to display Fibonacci series using recursion

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
n = int(input("Enter a number to obtain a sequence : "))
if n < 0:
    print("Enter a positive number : ")
else:
    print("Fibonacci sequence : ")
    for i in range(n):
        print(fibo(i))