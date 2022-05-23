#!/usr/bin/python3
"""
Module that extend script
0-gather_data_from_an_API.py
to Records all tasks that are
owned by this employee
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    user_r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                          .format(argv[1])).json()
    all_r = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    total_task = 0
    done_task = bool
    tasks = []

    for i in all_r:
        if i["userId"] == user_r["id"]:
            total_task += 1
            if i["completed"] is True:
                done_task = True
            else:
                done_task = False
            tasks.append([user_r['id'], user_r['username'],
                         done_task, i['title']])

    with open("{}.csv".format(user_r["id"]), "wt", encoding="UTF8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks)
