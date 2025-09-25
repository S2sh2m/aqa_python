class Student:
    def __init__(self, name=None, last_name=None, age=None, average_ball=None):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.average_ball = average_ball

    def change_avr(self, new_average):
        self.average_ball = new_average

    def print_info(self):
        print(f"Студент: {self.name} {self.last_name}, "
              f"вік: {self.age}, середній бал: {self.average_ball}")


student1 = Student("Alex", "Melnyk", 20, 4.5)

student1.print_info()

student1.change_avr(3.8)

student1.print_info()

