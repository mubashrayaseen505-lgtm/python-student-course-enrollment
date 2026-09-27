# Student Course Enrollment System

A beginner-friendly Python project that demonstrates Object-Oriented Programming through a simple student course enrollment system.

## Features

- Create student objects
- Create course objects
- Display student information
- Display course information
- Enroll a student in a course
- Check course seat availability
- Automatically decrease available seats after enrollment
- Handle courses with no available seats

## OOP Concepts Used

This project demonstrates:

- Classes and objects
- `__init__()` constructor
- Instance attributes
- Instance methods
- Passing objects as arguments
- Interaction between multiple classes
- Updating object attributes
- Conditional statements

## How It Works

The project contains two main classes.

### Student

The `Student` class stores:

- Student name
- Roll number

The student can also enroll in a course.

### Course

The `Course` class stores:

- Course name
- Teacher name
- Available seats

The course keeps track of the number of seats remaining.

When a student successfully enrolls, the available seats decrease by one.

## Example

The course starts with:

```text
Course Name: Python Programming
Teacher Name: Harry
Available Seats: 2
