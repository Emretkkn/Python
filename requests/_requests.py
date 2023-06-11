import requests
import json
result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)
# print(result[0]["userId"])
for i in result:
    if i["userId"] > 3 and i["userId"] < 8:
        print(i["completed"])