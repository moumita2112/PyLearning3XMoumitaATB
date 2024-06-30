# Filters in python
# Filters work only with functions
# Filters take arguments as function and list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def is_even(num):
    return num % 2 == 0


new_list = filter(is_even, numbers)
print(list(new_list))


def is_odd(m):
    return m % 2 != 0


more_list = filter(is_odd, numbers)
print(list(more_list))


def greater_five(n):
    return n > 5


m_list = filter(greater_five, numbers)
print(list(m_list))
