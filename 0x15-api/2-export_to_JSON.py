#!/usr/bin/python3
"""
Script fetches and displays the TODO list progess
of given employee from JSONPlacehlder API.
"""

import json
import requests
import sys


def get_employee_todo_progress(emp_id):
    # Fetching user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    response = requests.get(user_url)
    user = response.json()

    # Fetching user's todo  list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    response = requests.get(todos_url)
    todos = response.json()

    # Calculating the number of completed & total tasks
    comp_tasks = [todo for todo in todos if todo.get('completed')]
    tot_tasks = len(todos)
    done_tasks = len(comp_tasks)

    # Prep data for JSON export
    tasks_data = [{
        "task": todo.get('title'),
        "completed": todo.get('completed'),
        "username": user.get('username')
        } for todo in todos]

    json_data = {str(emp_id): tasks_data}

    # Exporting data to JSON
    json_filename = f"{emp_id}.json"
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file)

if __name__ == "__main__":
    # Ensuring a valid employee ID is provided
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./2-export_to_JSON <emplyee_id>")
    else:
        emp_id = int(sys.argv[1])
        get_employee_todo_progress(emp_id)
