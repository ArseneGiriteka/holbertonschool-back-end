#!/usr/bin/python3
"""This module gathers data from an API"""


import requests
import sys

def get_employee_todo_list_progress(employee_id):
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data['name']

    total_tasks = len(todos_data)
    completed_tasks = len([todo for todo in todos_data if todo['completed']])

    print(f'Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):')

    for todo in todos_data:
        if todo['completed']:
            print('\t ' + todo['title'])

employee_id = sys.argv[1]

get_employee_todo_list_progress(employee_id)
