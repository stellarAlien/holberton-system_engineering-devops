#!/usr/bin/python3
"""_summary_
    return each employee's todo list
    Returns:
        employee progress    
"""
import requests
import sys


if __name__ == '__main__':

    id = sys.argv[1]
    title = []
    com = 0
    total = 0
    url = "https://jsonplaceholder.typicode.com/users/" + id
    result = requests.get(url).json()
    name = result.get('name')
    url = "https://jsonplaceholder.typicode.com/todos/"
    result2 = requests.get(url).json()
    for r in result2:
        if r.get('userId') == int(id):
            if r.get('completed') is True:
                title.append(r['title'])
                com += 1
            total += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, com, total))
    for s in title:
        print("\t {}".format(s))
