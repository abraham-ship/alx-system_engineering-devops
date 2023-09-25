#!/usr/bin/python3

if __name__ == '__main__':
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com"

    response = requests.get(url + f"/users/{argv[1]}")

    user_info = response.json()
    employee_name = user_info["name"]

    todo_url = url + f"/todos?userId={argv[1]}"
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task["completed"])

    print(f"Employee {employee_name} is done with tasks\
            ({completed_tasks}/{total_tasks}):")

    for task in todo_list:
        if task["completed"]:
            print(f"\t{task['title']}")
