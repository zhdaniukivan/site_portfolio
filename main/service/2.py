import random
import time

# class Person:
#     def __init__(self, name, age, job):
#         self.name = name
#         self.age = age
#         self.job = job
#
#     def get_all_inform_about_person(self):
#         return f'Сотрудник {self.name} имеет возраст {self.age} занимает должность {self.job}'
#
#     def __del__(self):
#         print( f'Досвидания {self.name}')
#
# bob = Person('Bob', 22, 'manager')
# sndy = Person('Sendy', 22, 'manager')
# lesly = Person('lesly', 22, 'manager')
# print(bob.get_all_inform_about_person())
# input()


# class Warrior:
#     def __init__(self, name, health = 100):
#         self.health = health
#         self.name = name
#
#     def get_hit(self):
#         self.health = self.health - 20
#         return self.health
#
#
#     def check_health(self):
#         if self.health >= 0:
#             print(f'Воин жив у него еще {self.health} HP')
#         else:
#             print(f'Вони погиб {self.name} :-(')
#
# bob = Warrior('Bob')
# sandy = Warrior('Sandy')
# while bob.health > 0 and sandy.health > 0:
#     print(bob.health, sandy.health)
#     time.sleep(2)
#     some_random_int = random.randint(0, 99)
#     print(some_random_int)
#     if some_random_int % 2 != 0:
#         print(f'Здоровье {bob.name} {bob.get_hit()}')
#
#     else:
#         print(f'Здоровье {sandy.name} {sandy.get_hit()}')


class People:
    def __init__(self, name, age, status, group=None):
        self.name = name
        self.age = age
        self.status = status
        self.group = group




class Student(People):
    pass




class Teacher(People):
    def teach(self, info, *kwargs):
        for student in kwargs:
            student.




