#  Program to find numbers divisible by another number

l = [12,13,25,26,29,39]
print("The numbers are divisible by 13 are :")
result = list(filter(lambda x : x % 13 == 0,l))
print(result)

# using for loop
n = int(input("Enter the Number : "))
if n == 0 : 
    print("Invalid input")
else:
    print("Numbers are divisible by 13")
    for i in range(1,n+1):
        if i % 13 == 0:
            print(i)
