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

`POST /todos`
```
Sample Response:
{
    "done": false,
    "id": 2,
    "title": "wash the dishes"
}
```

- Get all Todo Items

`GET /todos`
```
Sample Response:
[
    {
        "done": false,
        "id": 1,
        "title": "wash the dishes"
    },
    {
        "done": false,
        "id": 2,
        "title": "feed the dogs"
    }
]
```

- Get a single Todo Item

`GET /todos/{todo_id}`
```
Sample Response:
{
    "done": false,
    "id": 2,
    "title": "wash the dishes"
}
```

- Mark Todo Item as done

`/todos/{todo_id}/done`
```
Sample Response:
{
    "done": true,
    "id": 2,
    "title": "wash the dishes"
}
```

- Clear all Todo Items

`POST /todos/clear`
```
{
    "message": "Todo list cleared successfully"
}
```

 # Technologies used
- Flask

# Tests
- To run tests
> `python -m pytest`
> 
- View Test Coverage

To generate test coverage report, run:
>  coverage run -m pytest

- To view test coverage report
> coverage report

- Run test with 80% threshold coverage checked

Run this first:
> export PYTHONPATH=$(pwd)

Then run:
> pytest --cov=app --cov-report=xml:coverage.xml --cov-report=term --cov-fail-under=80