# school.py

class Person:
    def __init__(self, name: str, age: int, country: str):
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f"{self.name} is {self.age} years old and is from {self.country}."


class Student(Person):
    def __init__(self, name: str, age: int, country: str, major: str, gpa: float):
        super().__init__(name, age, country)
        self.major = major
        self.gpa = gpa

    def study(self):
        return f"{self.name} is studying {self.major} with a current GPA of {self.gpa}."


class Staff(Person):
    def __init__(self, name: str, age: int, country: str, position: str, department: str):
        super().__init__(name, age, country)
        self.position = position
        self.department = department

    def work(self):
        return f"{self.name} works as a {self.position} in the {self.department} department."


# Demonstration calls (for manual testing or demo purposes)
if __name__ == "__main__":
    # Creating objects
    person = Person("Alex", 30, "USA")
    student = Student("Maria", 20, "Canada", "Computer Science", 3.8)
    staff = Staff("Dr. Smith", 45, "UK", "Professor", "Engineering")

    # Method calls
    print(person)
    print(student.study())
    print(staff.work())
