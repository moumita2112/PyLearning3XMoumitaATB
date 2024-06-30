my_dict = {'a': 1,
           'b': 2,
           'c': 3,
           'd': 4}
#find the elements in a dictionary using for loop
for (k, v) in my_dict.items():
    if k == 'd':
        print("Value of d is found in my_dict")
#find the elements using another method
op = 'b' in my_dict.items()
print(op)
