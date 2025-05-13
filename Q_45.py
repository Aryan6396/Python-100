# Program to sort a dictionary by value

marks = {'John': 90, 'Emma': 85, 'Sophia': 95, 'Michael': 80}
# Sort the dictionary by value in ascending order  
sorted_marks = dict(sorted(marks.items(), key=lambda item: item[1]))
print("Sorted dictionary by value in ascending order:")
print(sorted_marks)