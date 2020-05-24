# Создайте класс Student, который содержит атрибуты: фамилия и инициалы,
# номер группы, успеваемость (dict из элементов).
# Создать класс Group с атрибутом name,
# Свяжите эти 2 класса путем инициализации класса Group в классе Student

class Group():
    def __init__(self, name):
        self.name = name

class Student():
    def __init__(self, surname, name, group, progress):
        self.surname = surname
        self.name = name
        self.group = Group(group)
        self.progress = progress

# Создать 5 студентов с разными именами, с любым количеством предметов, с оценками 1-5.
# Они могут быть студентами одной группы.
# Создать класс генератор результатов, который будет принимать на вход данные о студентах
# и иметь возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.
# Метод создания экземпляров класса Students поместите в один из методов класса генератора результатов.

class UserInfoAggregator():
    def __init__(self, data_context):
        self.students = data_context

    def studentmaker(self):
        return [Student(surname, name, group, progress) for surname, name, group, progress in self.students]

    def goodstudents(self):
        for s in self.studentmaker():
            if min(s.progress.values()) > 3:
                print(s.surname, s.group.name)

# student1 = Student("Jackson", "Peter", "A1", {"Math": 10, "Physics": 10})

students = [("Chan", "Cheng", "A1", {"Math": 5, "Physics": 4}),
            ("Zhou", "Yang", "A2", {"Math": 4, "Physics": 4}),
            ("Rogue", "Jean", "A1", {"Math": 3, "Physics": 5})]

s_list = UserInfoAggregator(students)
# print(s_list.studentmaker()[0].group.name)
s_list.goodstudents()