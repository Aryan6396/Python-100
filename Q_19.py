# Program to display power of 2 using anonymous function

nterms = int(input("Enter the number : "))

result = list(map(lambda x: x**2 , range(nterms+1)))

for i in range(nterms+1):
    print(f"The value of 2 raise to power {i} = {result[i]}")
