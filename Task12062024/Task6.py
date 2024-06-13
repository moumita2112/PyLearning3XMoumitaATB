#Fibonacci Series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 1, 2, 3, 5, 8
number = int(input("Enter the range of Fibonacci Series: "))
a = 0
b = 1
for i in range(number):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

