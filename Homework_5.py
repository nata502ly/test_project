class Employee:
    def __init__(self, name=None, position=None, salary=0, experience = 0):
        self.name = name
        self.position = position
        self.salary = salary
        self.experience = experience
    def set_name(self, name):
        self.name = name
    def set_position(self, position):
        self.position = position
    def set_salary(self,salary):
        self.salary = salary
    def set_experience(self, experience):
        self.experience = experience
    def calculate_income(self, months):
        return int(self.salary) * int(months)
    def position(self, experience):
        if experience <=3:
            return "Junior"
        elif 3<experience<=6:
            return "Middle"
        else:
            return "Senior"


obj1 = Employee("Natasha", "QA")
obj2 = Employee(name="Bob",salary=1000)
obj3 = Employee(experience = 5)
print(obj2.calculate_income(10))
print(obj1.position)
print(obj3)


