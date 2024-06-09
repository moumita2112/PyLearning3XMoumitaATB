# List - Shopping List
# milk, bread, butter, poha
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit


shopping_list = ["milk","biscuit","choclates", "bread", "butter", "poha"]
print(shopping_list)
print(len(shopping_list)) #5
print(shopping_list[0])#milk
print(shopping_list[-1])#poha

shopping_list.append("curd") # Add item in the end
print(shopping_list)
shopping_list.insert(3, "jam") # Add item in the middle
print(shopping_list)

shopping_list.extend(["chips", "salt","sugar"]) # Add multiple items in the end
print(shopping_list)

shopping_list.remove("sugar") # Remove item
print(shopping_list.pop())
print(shopping_list.index("butter"))
shopping_list.reverse()
shopping_list.sort()
print(shopping_list)
shopping_list[0] ="Moumita"
print(shopping_list)

#
my_list = [1, 2, 3, 4, True, 3.14, "Pramod"]
print(type(my_list))  # <class 'list'>