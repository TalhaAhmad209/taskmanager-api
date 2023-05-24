# Task Manager API

The Task Manager API is an API for managing tasks or to-do lists. It allows users to create, update, and delete tasks, as well as mark them as complete and assign them to specific categories.

## Features

- User registration and authentication using JWT (JSON Web Tokens)
- Create, update, and delete tasks
- Mark tasks as complete
- Assign tasks to specific categories

## Technologies Used
- Django: a high-level Python web framework
- Django REST Framework: a powerful and flexible toolkit for building Web APIs
- Django REST Framework SimpleJWT: a library for JWT authentication with Django REST Framework

## Installation

1. Clone the repository:

```bash
$ git clone https://github.com/TalhaAhmad209/taskmanager-api.git
$ cd taskmanager-api
```

2. Set up a virtual environment:

```python
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Install the dependencies:

```python
pip install -r requirements.txt
```

4. Run the migrations:

```python
python manage.py migrate
```

5. Run the migrations:

```python
python manage.py runserver
```



# Usage
## Register a user:

Send a POST request to /api/register/ with the following payload:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
## Obtain JWT Token (Authentication):

Send a POST request to /api/token/ with the following payload:
```json
Copy code
{
  "username": "your_username",
  "password": "your_password"
}
```
The response will include a JWT token:
```json
Copy code
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```
## Create a category:

Send a POST request to /api/categories/ with the following payload:
```json
{
  "name": "Category Name"
}
```

Include the JWT access token obtained in the previous step in the Authorization header of the request.

Add a task:

Send a POST request to /api/tasks/ with the following payload:
```json
{
  "title": "Task Title",
  "description": "Task Description",
  "completed": false,
  "category": 1
}
```

Include the JWT access token obtained in the previous step in the Authorization header of the request.

Make sure to provide a valid category ID (category) obtained in the previous step.

