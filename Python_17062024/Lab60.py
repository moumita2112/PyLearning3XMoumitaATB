def sum_three_numbers(a=9, b=1, c=0):
    return a + b + c


result1 = sum_three_numbers()
result2 = sum_three_numbers(1, 2)
result3 = sum_three_numbers(3, 5, 6)
result4 = sum_three_numbers(5)
result5 = sum_three_numbers(a=8, c = 10, b=2)
print("Sum of three:", result1, result2, result3, result4, result5)
