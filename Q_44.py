# Program to iterate over Dictionaries using for loop

dict = {
    'name':'John',
    'age':25,
    'city':'New York'
}

# Solution 1 with .items()
for key, value in dict.items():
    print(key, ":", value)