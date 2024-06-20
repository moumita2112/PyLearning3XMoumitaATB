def find_odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


find_odd_even(2)

# using lamda expression
find_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(find_even_odd(5))
