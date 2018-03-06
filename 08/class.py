class Person:
    pass

class Student:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('hello, i\'m {0}'.format(self.name))

# p = Person()
# print(Person)
# print(p)

stu = Student('LiLei')
stu.say_hi()

