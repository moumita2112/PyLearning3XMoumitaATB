# #Block of code which can be re-used
# #Build-in functions are present in builtins.py file
# Define
# Call

res = max(6, 9)
print(res)


# #user defined functions
# #They can return something
# They can't return anything> non-return
# They have parameters
# The don't have parameters


def say_hello():  # No return type, no paramter/argument
    print("Hello")


say_hello()


def say_hello(name):  # No return type with parameter/argument
    print("your name is:", name)


say_hello("Moumita")
say_hello("Amit")


def say_hello_again(name="Vivaan"):  # No return type with default parameter/argument
    print("Your name is:", name)


say_hello_again("Moumita Chakraborty")
say_hello_again(name="Padmashri")
say_hello_again("Poorav")
say_hello_again()


def say_hello_with_return(m, n): #With parameter and return type
    return m + n


result = say_hello_with_return(3, 4)
result = say_hello_with_return(m=99, n=100)
result = say_hello_with_return(n=1, m=1)
print(result)
