def fizz_buzz(number):
    if number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0 & number % 5 == 0:
        print('FizzBuzz')
    else:
        print(number)


fizz_buzz(int(input()))

lst = [5, 10, 20]
try:
    print(lst)
except IndexError:
    print("Something went wrong")


class Jet:
    def name(self):
        return 'name', self

    def country(self):
        return 'country', self


print(Jet.name('B-52'), Jet.country('USA'))

print(Jet.name('MiG-21'), Jet.country('Russia'))


def show_numbers(limit):
    for i in range(0, limit):
        if i % 2 == 0:
            print(i, 'EVEN')
        else:
            print(i, ' ODD')


show_numbers(int(input()))


class Person:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def print_name(self):
        print(self.firstname, self.lastname)


person1 = Person("Malek", "Jan")
person1.print_name()

while True:
    try:
        int(input("Please enter name: "))
        break
    except ValueError:
        print("Invalid! your name should be number!")
print("Right naming!")


class Student:
    pass


class Marks(Student):
    pass


s = Student()
m = Marks()
print(isinstance(s, Student))
print(isinstance(m, Student))
print(isinstance(m, Marks))
print(isinstance(s, Marks))
print('not subclass', issubclass(Student, Marks))
print('subclass', issubclass(Marks, Student))
