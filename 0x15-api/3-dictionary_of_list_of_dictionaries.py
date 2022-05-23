#!/usr/bin/python3
"""
Module that Records all tasks
from all employees in a JSON file
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    user_r = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    all_r = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    total_task = 0
    done_task = bool
    tasks = {}

    for i in user_r:
        tasks[i['id']] = []
        for j in all_r:
            if j["userId"] == i["id"]:
                tasks[i['id']]\
                    .append({"username": i['username'], "task": j['title'],
                            "completed": j['completed']})

    with open("todo_all_employees.json", "wt", encoding="UTF8") as file:
        json.dump(tasks, file)
