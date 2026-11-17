# Library Management System

A desktop application for managing a library system developed with Python and PySide6.

## Description

Library Management System is an object-oriented application that allows users to manage books, users, and loans through a graphical interface.

The project focuses on clean architecture, data management, and the implementation of real-world software development practices.

## Features

### Book management
- Add new books
- Update book information
- Delete books
- Search and display books
- Manage book availability

### User management
- Add and manage library users
- Store user information
- Search users

### Loan management
- Borrow books
- Return books
- Track borrowing and return dates
- Detect late returns

### Data persistence
- Save library data in JSON format
- Load data automatically when starting the application

## Architecture

The project follows an object-oriented design:
library-management/
│
├── models/
│   ├── Book
│   ├── User
│   ├── Loan
│   └── Library
│
├── views/
│   ├── MainWindow
│   ├── BooksTab
│   ├── UsersTab
│   └── LoansTab
│
└── data/
└── library.json



## Technologies

- Python 3
- PySide6 (Qt Framework)
- Object-Oriented Programming
- JSON data storage
- Git / GitHub

## Concepts implemented

- Classes and objects
- Encapsulation
- Inheritance
- Type hints
- Exception handling
- File management
- GUI development
- Separation between business logic and user interface

## Future improvements

- Add database support (SQLite/PostgreSQL)
- Add authentication system
- Improve UI design with Qt Style Sheets
- Export reports
- Add advanced search filters
