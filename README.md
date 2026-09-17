# Student Management System

## Project Description

The Student Management System is a web-based application developed using Python and Django. It helps administrators manage student information in a simple and organized way.

The system allows users to add, view, edit, delete, and search student records. It also provides a Django Admin Panel for database management.

## Objectives

- To maintain student information digitally.
- To reduce manual record management.
- To make student information easy to access.
- To perform CRUD operations efficiently.
- To provide a simple and user-friendly interface.

## Features

- Add Student
- View Student List
- Edit Student Details
- Delete Student
- Delete Confirmation
- Search by Name, Email, or Department
- Total Student Count
- Duplicate Email Validation
- Success and Error Messages
- Django Admin Panel

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Visual Studio Code

## Database

The project uses SQLite as the database.

The main student information includes:

- Student ID
- Name
- Email
- Phone
- Address
- Department

## CRUD Operations

### Create
Add new student details to the system.

### Read
View all student records in the student list.

### Update
Edit and update existing student information.

### Delete
Delete student records after confirmation.

## Search

The application provides a search option to find students using:

- Name
- Email
- Department

## Project Structure

```text
student_management/
│
├── configuration/
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
└── README.md
How to Run the Project
Step 1: Open the Project

Open the following folder in VS Code:

C:\xampp\htdocs\student_management
Step 2: Open Terminal

Run:

python manage.py runserver
Step 3: Open the Website

Open this address in your browser:

http://127.0.0.1:8000/
Step 4: Django Admin

Open:

http://127.0.0.1:8000/admin/
Advantages
Simple and easy to use.
Reduces manual record management.
Easy to search student information.
Supports complete CRUD operations.
Uses Django and SQLite.
Provides Django Admin for database management.
Future Enhancements

The project can be improved by adding:

Student login and registration
Student profile
Attendance management
Marks and result management
Pagination
Export student data
User authentication and permissions
Author

Sibisha

Purpose

This project was developed as a college project to demonstrate CRUD operations and web application development using Python, Django, HTML, CSS, and SQLite.


### 2. In VS Code

Open **README.md** → press **Ctrl + A** → delete the old content → **paste** this → press **Ctrl + S**.

That's all for this step. 👍