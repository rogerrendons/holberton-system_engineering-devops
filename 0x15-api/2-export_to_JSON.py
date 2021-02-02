#!/usr/bin/python3
""" Exports from REST to JSON """
if __name__ == "__main__":
    import json
    import requests
    import sys

    JasonList = []
    Dictio = {}

    ID_User = sys.argv[1]
    User = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(ID_User)).json().get("username")
    url = 'https://jsonplaceholder.typicode.com/todos/?userId='
    ToDo = requests.get(url + ID_User).json()

    for ToDoRec in ToDo:
        JasonDict = {}
        JasonDict["task"] = ToDoRec.get("title")
        JasonDict["completed"] = ToDoRec.get("completed")
        JasonDict["username"] = User
        JasonList.append(JasonDict)
    Dictio[ID_User] = JasonList

    with open('{}.json'.format(ID_User), 'w') as FileJason:
        FileJason.write(json.dumps(Dictio))
