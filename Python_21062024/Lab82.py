# Unpacking of tuple

(a, b, c) = (12, 34, 56)

# Append in tuple

t = (23, 45, 89)
new_tuple = t + (3,)
print(new_tuple)

moumita_list = list(new_tuple)
print(moumita_list)
moumita_list.append(2)
new_t2 = tuple(moumita_list)
print(new_t2)
