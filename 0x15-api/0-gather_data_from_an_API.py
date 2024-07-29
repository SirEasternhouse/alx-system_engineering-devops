#!/usr/bin/python3
"""
Script fetches and displays the TODO list progess
of given employee from JSONPlacehlder API.
"""


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

    # Printing the results
    emp_name = user.get('name')
    print(f"Employee {emp_name} is done with tasks({done_tasks}/{tot_tasks}):")
    for task in comp_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    # Ensuring a valid employee ID is provided
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API <emplyee_id>")
    else:
        emp_id = int(sys.argv[1])
        get_employee_todo_progress(emp_id)
