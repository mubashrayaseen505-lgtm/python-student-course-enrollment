class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)

    # Student enrolls in a Course object
    def enroll_course(self, course):
        if course.available_seats > 0:
            print(f"{self.name} enrolled in {course.course_name} successfully.")
            course.available_seats -= 1
        else:
            print("No seats left.")


class Course:
    def __init__(self, course_name, teacher_name, available_seats):
        self.course_name = course_name
        self.teacher_name = teacher_name
        self.available_seats = available_seats

    def display(self):
        print("Course Name:", self.course_name)
        print("Teacher Name:", self.teacher_name)
        print("Available Seats:", self.available_seats)


# Create objects
student1 = Student("Ali", 101)
course1 = Course("Python Programming", "Harry", 2)

# Display initial information
student1.display()
course1.display()

print()

# Enroll student
student1.enroll_course(course1)

print()

# Display course again to see updated seats
course1.display()
