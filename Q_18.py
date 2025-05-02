# Program to find the sum of all numbers

num1 = int(input("Enter the limit = "))

sum = 0
for num in range(1,num1+1):
    sum = sum+num
    # print(f"{num}+",end="")
print(sum)