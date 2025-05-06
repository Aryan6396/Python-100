# Program to sort words in Alphabetic order

word = input("Enter sentence : ")

split = word.split()

for i in range(len(split)):
    split[i] = split[i].lower()

split.sort()
print("String in alphabetic order")
for i in split:
    print(i)