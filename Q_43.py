# Program to access index of a list using for loop
# using enumerate
l = [10,2,22,12,14,188,1,0,2,3,5,1,5,6,2,6,5623,56]

for i,value in enumerate(l,start=1):
    print("index =",i,"and value = ",value)


for i in range(len(l)):
    value = l[i]
    print(i,value)