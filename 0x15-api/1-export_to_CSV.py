#!/usr/bin/python3
"""
script to export data in the CSV format from task #0
"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    employee = user.get("username")
    tasks = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId=\
            {user_id}").json()

    with open("{user_id}.csv", mode='w') as f:
        fh = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            fh.writerow([user_id, employee, task.get("completed"),
                         task.get("title")])
