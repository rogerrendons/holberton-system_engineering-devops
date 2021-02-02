#!/usr/bin/python3
""" Get list progress of a user. """
from csv import writer, QUOTE_ALL
from csv import QUOTE_ALL
from sys import argv
from requests import get

if __name__ == '__main__':
    DictUser = get(
        'https://jsonplaceholder.typicode.com/users/{:s}'
        .format(argv[1])).json()
    ToDo = get(
        'http://jsonplaceholder.typicode.com/todos?userId={:s}'
        .format(argv[1])).json()

    with open('{:s}.csv'.format(argv[1]), mode='w') as ToDo_File:
        ToDoList = writer(ToDo_File, delimiter=',', quotechar='"',
                          quoting=QUOTE_ALL)
        for Rec in ToDo:
            ToDoList.writerow([DictUser['id'], DictUser['username'],
                               Rec['completed'], Rec['title']])
