#!/usr/bin/python3
"""This module gathers data from an API"""


import requests
import sys


def get_employee_todo_list_progress(employee_id):
    """Prints the progress of a given employee's todo list"""
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    user_data = user.json()
    todos_data = todos.json()

    employee_name = user_data['name']

    total_tasks = len(todos_data)
    completed_tasks = len(
        [todo for todo in todos_data if todo['completed']])

    str1 = f"f'Employee {employee_name} is done with tasks"
    str2 = f"({completed_tasks}/{total_tasks}):"
    print(str1 + str2)

    for todo in todos_data:
        if todo['completed']:
            print('\t ' + todo['title'])


if __name__ == "__main__":
    try:
        employee_id = sys.argv[1]
        get_employee_todo_list_progress(employee_id)
    except Exception as e:
        pass
