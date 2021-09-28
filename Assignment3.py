NumList = []

Number = int(input("Enter the total number of integers:"))
for i in range(1, Number +1):
    value = int(input("Please enter the values of %d elements: " %i))
    NumList.append(value)

print("\n Positive numbers in this list are: ")
for j in range(Number):
    if(NumList[j] >=0):
        print(NumList[j], end= '\n')

NumList = []

Number = int(input("\t \n Enter the total number of integers:"))
for i in range(1, Number +1):
    value = int(input("Please enter the values of %d elements: " %i))
    NumList.append(value)

print("\n Positive numbers in this list are: ")
for j in range(Number):
    if(NumList[j] >=0):
        print(NumList[j], end= '\n')
