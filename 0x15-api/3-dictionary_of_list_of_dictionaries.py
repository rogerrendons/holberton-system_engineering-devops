#!/usr/bin/python3
"""Exports from JSON"""
import json
import requests


if __name__ == "__main__":
    Dict = {}

    url = "https://jsonplaceholder.typicode.com/"
    Usr = requests.get("{}users".format(url)).json()
    ToDo = requests.get("{}todos".format(url)).json()

    for Users in Usr:
        List = []
        for Rec in ToDo:
            if Rec.get('userId') == Users.get('id'):
                task_dict = {"username": Users.get('username'),
                             "task": Rec.get('title'),
                             "completed": Rec.get('completed')}
                List.append(task_dict)
        Dict[Users.get('id')] = List

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(Dict, f)
