#!/usr/bin/python3
"""
Module that exports data in the
JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    user_r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                          .format(argv[1])).json()
    all_r = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    total_task = 0
    done_task = bool
    tasks = {}
    tasks[user_r['id']] = []

    for i in all_r:
        if i["userId"] == user_r["id"]:
            total_task += 1
            if i["completed"] is True:
                done_task = True
            else:
                done_task = False

            tasks[user_r['id']]\
                .append({"task": i['title'], "completed": done_task,
                        "username": user_r['username']})

    with open("{}.json".format(user_r["id"]), "wt", encoding="UTF8") as file:
        json.dump(tasks, file)
