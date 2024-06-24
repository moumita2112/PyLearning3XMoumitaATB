my_set = {"https://testingacademy.com", "https://testingacademy.com", "www.google.com"}
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7, 8, 9}
print(set1.union(set2))

set1 = {222, 3, 5, 7, 8, 9, 0}
set2 = {222, 0, 3, 55, 666, 43, 333}
print(set1.intersection(set2))

setm = {1, 5, 89, 555, 6, 677}
setn = {1, 222, 3, 4, 555, 3, 45, 677}
print(setm.difference(setn))
print(setn.difference(setm))
