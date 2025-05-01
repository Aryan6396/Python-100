# Program to print all prime numbers in an interval

num1 = int(input("Enter the lower limit = "))
num2 = int(input("Enter the upper limit = "))

for num in range(num1,num2 + 1):
    if num > 1:
        for i in range(2,num):
            if num % i ==0:
                break
        else:
            print(num)