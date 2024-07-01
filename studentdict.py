class Student:
    def _init_(self, student_id, name):
        self.student_id = student_id
        self.name = name
num_students = int(input("How many students need to be created? "))
students = {}
for i in range(num_students):
    student_id = input(f"Enter ID for student {i + 1}: ")
    name = input(f"Enter name for student {i + 1}: ")
    student = Student(student_id, name)
    students[student_id] = student
for student_id, student in students.items():
    print(f"Student ID: {student.student_id}, Name: {student.name}")