# Python Library Management System

A terminal-based library management system developed in Python as part of a programming course.

The application allows users to manage books, register library members, track book loans, and generate statistics through a simple command-line interface.

## Features

- List available and borrowed books
- Add and remove books
- Register and remove library members
- Borrow and return books
- Search for books by title or author
- View library statistics
- Export statistics to a text file
- Automatically create required data files

## Technologies

- Python 3
- Standard Python libraries (`pathlib`, `contextlib`)
- Text-file storage using semicolon-separated values
- Command-line interface (CLI)

## Getting Started

**Requirements:** Python 3 installed on your computer.

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run the application:

   `python Bibliotek.py`

On systems where Python 3 is accessed through `python3`, use:

   `python3 Bibliotek.py`

The application automatically creates `books.txt`, `users.txt`, and `loans.txt` if they do not already exist.

## Project Background

This project was developed as a school assignment to practice Python fundamentals, including functions, loops, conditional statements, file handling, input validation, and basic data management.

The application uses a text-based interface and does not require external Python packages.

## Language

The application's interface is currently in Swedish.
