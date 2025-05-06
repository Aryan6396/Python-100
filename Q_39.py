# Program to count the number of each vowel

string = input("Enter a string : ")
vowels = "aeiou"

string = string.casefold()
count = {}.fromkeys(vowels,0)

for char in string:
    if char in count:
        count[char] += 1

print(count)