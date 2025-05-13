# Program to concatenate two lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

# with unique elements
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 3]

list3 = list(set(list1 + list2))
print("Concatenated list with unique elements:", list3)

# using the extend() method
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("Concatenated list using extend():", list1)
