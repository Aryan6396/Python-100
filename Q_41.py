# Program to merge two dictionaries

dict1 = {'a': 10, 'b': 200}
dict2 = {'a': 250, 'y': 70}

print(dict1 | dict2)
print({**dict1,**dict2})

dict3 = dict2.copy()
dict3.update(dict1)

print(dict3)