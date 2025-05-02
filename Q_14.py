# Program to find a fatorial of a number

num = int(input("Enter a number : "))
fact = 1
for i in range(1,num+1):
    fact = fact *i
print(fact)

# Using recursion

def fact(a):
    if a == 0:
        return 1
    else:
        return a * (fact(a-1))
    
num  = int(input("Enter a number here : "))
result = fact(num)
print(result)