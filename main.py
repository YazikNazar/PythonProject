class Student:
    print('Hi')
    def __init__(self):
        self.height = 160
        self.money = 3000
        print(self)

nick = Student()
print(nick.height,'Height')
print(nick.money,'Money')