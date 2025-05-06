# Program to check whether a string is palindrome or not

a = str(input("Enter  a word to check palindrome : "))

rev = a[::-1]
print("reverse is: ",rev)
if a == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
