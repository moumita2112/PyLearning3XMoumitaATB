mimi_list = [2, 3, 4, 5, 6, 78]


def function_list():
    mimi_list.append(9)
    mimi_list.remove(2)
    print(mimi_list)


function_list()

# insert the list inside a function

moumi_list = [1, 3, 4, 556, 89]


def moumi_list_function(moum_list):
    moum_list.append(555)
    moum_list[1] = 345
    return moum_list


moumi_list_function(moumi_list)
print(moumi_list)
