# Program to find an armstrong number in an interval

num1 = int(input("Enter the lower limit = "))
num2 = int(input("Enter the upper limit = "))

for num in range(num1, num2+1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)