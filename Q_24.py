# Program to find factors of a number

num = int(input("Enter a number : "))
print(f"These numbers are factors of {num}")
factors = []
for i in range(1,num+1):
    if num % i == 0:
        factors.append(str(i))
print(",".join(factors))

