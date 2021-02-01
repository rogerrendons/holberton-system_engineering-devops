#!/usr/bin/python3
""" script given employee ID,returns list progress. """
import requests
from sys import argv


if __name__ == '__main__':
    All_Jason = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={"userId": argv[1]}).json()
    Users_Jason = requests.get(
        'https://jsonplaceholder.typicode.com/users',
        params={"id": argv[1]}).json()

    for Names in Users_Jason:
        EMPLOYEE_NAME = Names.get('name')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    for ToDo in All_Jason:
        if ToDo.get('completed'):
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(ToDo.get("title"))
        TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format
          (EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in TASK_TITLE:
        print("\t {}".format(i))
