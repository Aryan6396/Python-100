# Program to check if a list is empty

my_list = []
# Check if the list is empty
if not my_list:
    print("The list is empty.")
else:
    print("The list is not empty.")

# using the len() function
my_list = []    
# Check if the list is empty
if len(my_list) == 0:
    print("The list is empty.")
else:
    print("The list is not empty.")

# using the bool() function
my_list = []
# Check if the list is empty
if not bool(my_list):
    print("The list is empty.")
else:
    print("The list is not empty.")
