d = int(input("Enter the number\n"))
match d:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case 5:
        print("You have entered 5")
    case 6:
        print("You have entered 6")
    case _:
         print("I have no idea")

#real life example

browser= input("Enter the browser name:\n")
browser= browser.lower()
match browser:
    case 1:
        print("Chrome browser code is executed")
    case 2:
        print("Firefox browser code is executed")
    case 3:
        print("Safari browser code is executed")
    case _:
        print("Nothing is executed")