# Task - Factorial
# # 3. Factorial
# n = 5
# # 5! -->5*4*3*2*1 -> 120
# # 3! -> 3*2*1 -> 6
# # 4! -> 4*3*2*1 -> 24
import math

num = int(input("Enter the number:"))
print(math.factorial(num))

#using range

num2 = int(input("enter the number for which the factorial is to be found:"))
factorial = 1
if num2< 0:
    print("There is no factorial for negative numbers:")
elif num2== 0:
    print("Factorial of 0 is 1")
elif num2 >= 1:
    for i in range(1, num2 + 1):
        factorial = factorial * i
    print("Factorial of the  number is", factorial)
