#!/usr/bin/python3
"""
This module gathers data from an API and exports it to a JSON file
the file will cantain all task of all users
"""


import json
import requests
import sys


def do_jsonify():
    """
    returns a JSON string with all user's todo list progress
    """
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    all_users_tasks = {}

    for user in users.json():
        user_id = user['id']
        user_name = user['username']

        todos = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')

        tasks_list = []
        for todo in todos.json():
            task_dict = {"username": user_name,
                         "task": todo['title'],
                         "completed": todo['completed']}
            tasks_list.append(task_dict)

        all_users_tasks[user_id] = tasks_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(all_users_tasks, file)


if __name__ == "__main__":
    try:
        do_jsonify()
    except Exception as e:
        pass
