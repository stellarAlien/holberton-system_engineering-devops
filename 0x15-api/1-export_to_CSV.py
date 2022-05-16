#!/usr/bin/python3
"""

"""
import csv
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + id
    result = requests.get(url).json()
    username = result.get("username")
    req = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (id) + '/todos')
    with open("{}.csv".format(sys.argv[1]), "w") as file_csv:
        writer = csv.writer(file_csv, quoting=csv.QUOTE_ALL)
        for task in req.json():
            writer.writerow([id, username,
                            task.get("completed"), task.get("title")])
