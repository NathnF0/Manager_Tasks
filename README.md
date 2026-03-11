Multi User Task Manager (CLI)

A simple command-line task manager built with Python that supports multiple users.
Each user can manage their own tasks, which are stored locally using JSON persistence.

The application automatically generates demo users on first run so anyone can test the system immediately.

Features

Multi-user support

Create new users

Add tasks

List tasks

Mark tasks as completed

Edit existing tasks

Delete tasks

Persistent storage using JSON

Automatic demo data generation on first run

Technologies

Python

JSON file storage

Command Line Interface (CLI)

How to Run

Install Python on your machine.

Clone the repository:

git clone (https://github.com/NathnF0/Manager_Tasks.git)

Open the project folder.

Run the program:

python main.py
Demo Users

When the program runs for the first time, it automatically creates demo users:

demo1
demo2

These users already contain example tasks so you can test the system quickly.

Data Storage

All data is stored in a local JSON file:

tasks.json

This file is ignored by Git using .gitignore so every new user running the project will generate their own demo data.

Project Structure
multi-user-task-manager-cli
│
├── main.py
├── README.md
└── .gitignore
Future Improvements

Possible improvements for future versions:

User passwords

Task priorities

Due dates

Better terminal UI

Code modularization

License

This project is open source and available for learning and educational purposes.
