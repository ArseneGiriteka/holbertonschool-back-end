#!/usr/bin/python3
"""
This module gathers data from an API
and exports it to a JSON file
"""


import json
import requests
import sys


def do_jsonify(user_id):
    """
    returns a JSON string with the user's todo list progress
    """
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}')
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')

    user_name = user.json()['username']

    todo_list = []

    for todo in todos.json():
        task_dict = {}
        task_title = todo['title']
        task_status = todo['completed']
        task_dict = {"task": task_title,
                     "completed": task_status, "username": user_name}
        todo_list.append(task_dict)

    with open(f"{user_id}.json", "w") as file:
        json.dump({user_id: todo_list}, file)


if __name__ == "__main__":
    try:
        user_id = sys.argv[1]
        do_jsonify(user_id)
    except Exception as e:
        pass
