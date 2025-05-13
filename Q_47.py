# Program to catch multiple exceptions in one line


str_num = input("Enter a string: ")
# The above code will raise a TypeError because you cannot add an integer and a string.
# To catch multiple exceptions in one line, you can use a tuple to specify the exceptions you want to catch.
try:
    num = int(input("Enter a number: "))
    print(num + str_num)
except (TypeError, ValueError) as e:
    print("Error:", e)