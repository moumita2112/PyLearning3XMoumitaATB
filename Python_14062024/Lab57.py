def allowed_to_enter_python_class(name):
    match name:
        case "Moumita":
            print("Moumita is allowed")
        case "Python":
            print("Python is allowed")
        case "Mango":
            print("Mango is allowed")
        case _:
            print("Not allowed")
allowed_to_enter_python_class("python")
