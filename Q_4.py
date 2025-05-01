# Program Swap two variable (using third variable)

value_1 = int(input("value_1 = "))
value_2 = int(input("value_2 = "))
print(f"Values before swapping : value_1 = {value_1} value_2 = {value_2} ")
value_3 = value_1
value_1 = value_2
value_2 = value_3
print(f"Values after swapping : value_1 = {value_1} value_2 = {value_2} \n")


# Program Swap two variable (without using third variable)
value_1 = int(input("value_1 = "))
value_2 = int(input("value_2 = "))
print(f"Values before swapping : value_1 = {value_1} value_2 = {value_2} ")
value_1 = value_2 + value_1
value_2 = value_1 - value_2
value_1 = value_1 - value_2
print(f"Values after swapping : value_1 = {value_1} value_2 = {value_2} ")