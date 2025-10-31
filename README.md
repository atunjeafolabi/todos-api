# Basic Todo JSON API + Azure Pipelines

## Overview

This project is an implementation of a CI pipeline around a basic Todo web API that returns JSON data and built with Flask. It demonstrates
branching + PR workflow, build automation, unit testing with coverage, and static
analysis in CI. GitHub is used for source control and Azure Pipelines for CI.

The main focus of this project are as follows:
- Proper version control practices.
- Build automation setup.
- CI pipeline implementation.
- Branch protection and policies.
- Automated testing integration.

## Technologies used
- Python
- Flask
- Git and Github (version management)
- Azure Pipelines (CI)


## Local Development Setup

1) From the project root, create a virtual environment
> python3 -m venv venv

2) Activate the virtual environment:
> source venv/bin/activate

3) Install dependencies
> pip install -r requirements.txt`

4) Start the application locally
> flask --app main run

## Application Features
- Create a new todo item
- List a todo item
- List all todo items
- Mark a todo item as done
- Clear all items in todo list

## Endpoints
- Create a Todo Item

`POST /todos`
```
Response code: 201 CREATED

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
Response code: 200 OK

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
Response code: 200 OK

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
Response code: 200 OK

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
Response code: 200 OK

{
    "message": "Todo list cleared successfully"
}
```

## CI Pipeline Implementation
Azure pipelines used for CI. Code coverage of ≥ 80% (enforced)

## Branch Policies and Protection
- `Main` branch is protected and only the admin is authorized to merge development into `main` branch.

## Testing Strategy

#### To run tests
> `python -m pytest`
> 
#### View Test Coverage

To generate test coverage report, run:
>  coverage run -m pytest

#### To view test coverage report
> coverage report

#### Run test with ≥ 80% threshold coverage checked

Run this first:
> export PYTHONPATH=$(pwd)

Then run:
> pytest --cov=app --cov-report=xml:coverage.xml --cov-report=term --cov-fail-under=80

## Troubleshooting Guide
