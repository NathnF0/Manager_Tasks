📋 Multi User Task Manager (CLI)

Multi User Task Manager is a simple command-line task management system built with Python.
It supports multiple users, allowing each user to manage their own tasks independently.

All tasks are stored locally using JSON persistence, ensuring that data remains available between executions.

The application also generates demo users automatically on the first run so anyone can test the system immediately.

🚀 Features

Multi-user support

Create new users

Add tasks

List tasks

Mark tasks as completed

Edit existing tasks

Delete tasks

Persistent storage using JSON

Automatic demo data generation on first run

🧠 How It Works

Each user has their own list of tasks stored locally in a JSON file.

When the program starts, users can:

Select or create a user

Manage tasks through the command line interface

Update task status (complete, edit, delete)

The program automatically saves all changes to a JSON file, allowing task data to persist between sessions.

💻 Installation

Clone the repository:

git clone https://github.com/NathnF0/Manager_Tasks.git

Enter the project folder:

cd Manager_Tasks

Run the program:

python main.py
👥 Demo Users

When the program runs for the first time, it automatically creates demo users:

demo1
demo2

These users already contain example tasks so you can test the system quickly.

💾 Data Storage

All data is stored locally in a JSON file:

tasks.json

This file is ignored by Git using .gitignore, so every new user running the project will generate their own demo data automatically.

🛠 Technologies

Python

JSON file storage

Command Line Interface (CLI)

📂 Project Structure
multi-user-task-manager-cli
│
├── main.py
├── README.md
└── .gitignore
📌 Future Improvements

Possible improvements for future versions:

User authentication with passwords

Task priorities

Due dates

Improved terminal interface

Code modularization

📜 License

This project is open source and available for learning and educational purposes.
