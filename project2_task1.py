print("length of list1=")
m=int(input())
list1=[]
print("length of list2=")
n=int(input())
list2=[]

i=0
#entering list1 values
print("Enter numbers in list1=")
while i<m:
    list1.append(int(input()))
    i=i+1

i=0
#entering list2 values
print("Enter numbers in list2=")
while i<n:
    list2.append(int(input()))
    i=i+1

#checking for positive numbers in list1
print("Positive numbers in list1:")
for numbers in list1:
    if numbers>0:
        print(numbers)

#checking for positive numbers in list2
print("Positive numbers in list2:")
for numbers in list2:
    if numbers>0:
        print(numbers)