# Very important question : Lamda function

def new_function(salary):
    double_salary = salary * 2
    print(double_salary)


new_function(100)

# We can write the same using lamda function in 1 line

f_double_salary = lambda salary: salary * 2
print(f_double_salary(300))
