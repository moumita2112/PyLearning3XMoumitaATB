class Dog:
    name = None
    id = None
#Constructor: Constructor name is not same as class name , like java.It is always defined as def __init__(self,*args)
#Self is initial value
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def sleep(self):
        print("Who is Sleeping -> " + self.name)


dog1 = Dog("Chow", "1")
dog2 = Dog("Mow", "2")


print(f'{dog1.name} has ID {dog1.id}')
print(f'{dog2.name} has ID {dog2.id}')

dog1.sleep()
dog2.sleep()