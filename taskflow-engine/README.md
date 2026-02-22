#  TaskFlow Engine  
A clean, modular, and extensible command‑line task manager built with Python and SQLite.

TaskFlow Engine is a lightweight yet powerful CLI-based task management system designed with clean architecture principles.  
It provides a structured way to create, update, filter, and persist tasks using a modular architecture.

---

##  Features

- Add, update, delete tasks  
- Filter tasks by status, priority, or category  
- Persistent storage using SQLite  
- Modular architecture (CLI layer → service layer → data layer)  
- Fully testable with unit tests  
- Clean separation of concerns (SRP, OOP)

---

##  Project Structure

taskflow-engine/
│── cli/               # Command-line interface
│── core/              # Business logic (services, models)
│── data/              # SQLite database layer
│── tests/             # Unit tests
│── README.md
│── requirements.txt

---

##  Installation

```bash
git clone https://github.com/Davood-Portfolio/Python-Projects.git
cd taskflow-engine
pip install -r requirements.txt

 Usage
Add a task:
python cli/main.py add "Buy groceries" --priority high

Mark a task as done:

python cli/main.py done 3

 Running Tests
pytest

 Technologies Used
Python 3.x

SQLite

argparse

pytest

 License
MIT License
Feel free to use, modify, and contribute.