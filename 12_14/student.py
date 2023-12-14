import json
import os
 
class Student:
    """
    Represents a student with their student ID, name, and enrolled courses.
    """

    def __init__(self, student_id, name):
        """
        Initializes a new instance of the Student class.

        Args:
            student_id (int): The student's ID.
            name (str): The student's name.
        """
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def add_course(self, course_code, course_name, semester):
        """
        Adds a course to the student's enrolled courses.

        Args:
            course_code (str): The code of the course.
            course_name (str): The name of the course.
            semester (str): The semester in which the course is taken.
        """
        if semester not in self.courses:
            self.courses[semester] = []
        self.courses[semester].append({"code": course_code, "name": course_name})

    def delete_course(self, course_code, semester):
        """
        Deletes a course from the student's enrolled courses.

        Args:
            course_code (str): The code of the course.
            semester (str): The semester in which the course is taken.
        """
        if semester in self.courses and any(course["code"] == course_code for course in self.courses[semester]):
            self.courses[semester] = [course for course in self.courses[semester] if course["code"] != course_code]
            print(f"Course {course_code} deleted for {self.name} in semester {semester}.")
        else:
            print(f"Course {course_code} not found for {self.name} in semester {semester}.")

    def get_courses_by_semester(self, semester):
        """
        Retrieves the courses taken by the student in a specific semester.

        Args:
            semester (str): The semester.

        Returns:
            list: A list of dictionaries representing the courses taken in the specified semester.
        """
        return self.courses.get(semester, [])

    def save_to_file(self, filename):
        """
        Saves the student's information to a file.

        Args:
            filename (str): The name of the file to save the data to.
        """
        with open(filename, 'w') as file:
            data = {
                "student_id": self.student_id,
                "name": self.name,
                "courses": self.courses
            }
            json.dump(data, file)

    def load_from_file(self, filename):
        """
        Loads the student's information from a file.

        Args:
            filename (str): The name of the file to load the data from.
        """
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self.student_id = data["student_id"]
                self.name = data["name"]
                self.courses = data["courses"]
        else:
            print(f"File {filename} not found. Creating a new student profile.")
 
# Example usage:
student_id = "123456"
student_name = "John Doe"
student_filename = f"{student_id}_profile.json"
 
# Create or load student profile
student = Student(student_id, student_name)
student.load_from_file(student_filename)
 
# Add courses
student.add_course("CS101", "Introduction to Computer Science", "Fall 2023")
student.add_course("ENG201", "English Literature", "Fall 2023")
 
# Save the updated profile to file
student.save_to_file(student_filename)
 
# Display courses for a specific semester
semester_to_search = "Fall 2023"
courses_taken = student.get_courses_by_semester(semester_to_search)
print(f"Courses taken by {student_name} in {semester_to_search}:")
for course in courses_taken:
    print(f"{course['code']}: {course['name']}")
 
# Delete a course
course_to_delete = "CS101"
student.delete_course(course_to_delete, semester_to_search)
 
# Save the updated profile after course deletion
student.save_to_file(student_filename)