#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress
of all employees from the JSONPlaceholder API and
exports the data to a JSON file.
"""

import json
import requests


def get_all_employees_todo_progress():
    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(users_url)
    users = response.json()

    # Fetch all todos
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(todos_url)
    todos = response.json()

    # Preparing data for JSON export
    all_tasks_data = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        # Filtering todos fot current user
        user_tasks = [
                {
                    "username": username,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                    }
                for todo in todos if todo.get('userId') == user_id
                ]
        all_tasks_data[str(user_id)] = user_tasks

    # Exporting data to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(all_tasks_data, json_file)


if __name__ == "__main__":
    get_all_employees_todo_progress()
