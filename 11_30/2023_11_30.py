class Student:
    def __init__(self, school_name, department_name, dean_name, student_name, student_id, address, credits, gpa):
        self.school_name = school_name
        self.department_name = department_name
        self.dean_name = dean_name
        self.student_name = student_name
        self.student_id = student_id
        self.address = address
        self.credits = credits
        self.gpa = gpa

    def get_school_name(self):
        return self.school_name

    def set_school_name(self, school_name):
        self.school_name = school_name

    def get_department_name(self):
        return self.department_name

    def set_department_name(self, department_name):
        self.department_name = department_name

    def get_dean_name(self):
        return self.dean_name

    def set_dean_name(self, dean_name):
        self.dean_name = dean_name

    def get_student_name(self):
        return self.student_name

    def set_student_name(self, student_name):
        self.student_name = student_name

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, student_id):
        self.student_id = student_id

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_credits(self):
        return self.credits

    def set_credits(self, credits):
        self.credits = credits

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa

        # Create an instance of the Student class
student = Student("ABC School", "Computer Science", "John Doe", "Alice", "12345", "123 Main St", 60, 3.5)

# Get the sc
school_name = student.get_school_name()
print("School Name:", school_name)

# Set the department name
student.set_department_name("Information Technology")

# Get the updated department name
department_name = student.get_department_name()
print("Department Name:", department_name)

# Set the student ID
student.set_student_id("54321")

# Get the updated student ID
student_id = student.get_student_id()
print("Student ID:", student_id)
