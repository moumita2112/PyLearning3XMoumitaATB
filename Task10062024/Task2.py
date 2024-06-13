#square and cube of a number
num1 = int(input("Enter the num1"))

square = num1 ** 2
print(square)
cube = num1 ** 3
print(cube)

#Create a program that takes two numbers
# as input and prints whether the first number is greater than,
# less than, or equal to the second number.

firstnum= int(input("Enter the first number"))
secondnum= int(input("Enter the second number"))
if(firstnum== secondnum):
    print("First num is equal to second number")
elif(firstnum > secondnum):
    print("First num is greater than second number")
else:
    print("First num is less than second number")
