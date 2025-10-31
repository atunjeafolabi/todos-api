# Overview
This is a simple Todos web API that returns JSON.

# Installation

1) Create A Virtual Environment
> python3 -m venv venv

2) Activate the virtual environment:
> source venv/bin/activate

3) Install dependencies
> pip install -r requirements.txt`

4) Start the application locally
> flask --app main run

# Endpoints
- Create a Todo Item
> POST /todos

- Get all Todo Items
> GET /todos

- Get a single Todo Item
> GET /todos/{todo_id}

- Clear all Todo Items
> /todos/clear

 # Technologies used
- Flask

# Tests
To run tests
> `python -m pytest`