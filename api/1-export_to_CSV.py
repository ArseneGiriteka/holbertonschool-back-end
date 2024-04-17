#!/usr/bin/python3
"""This module gathers data from an API"""


import requests
import sys
import csv


def get_user_todo_list_progress(user_id):
    """Prints the progress of a given user's todo list"""
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}')
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')

    user_name = user.json()['username']

    for todo in todos.json():
        task = todo['title']
        task_status = todo['completed']
        with open(f'{user_id}.csv', mode='a', newline='') as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            csv_writer.writerow([user_id, user_name, task_status, task])


if __name__ == '__main__':
    try:
        user_id = sys.argv[1]
        get_user_todo_list_progress(user_id)
    except Exception as e:
        pass
