import requests

response = requests.get('http://127.0.0.1:5000/tasks/1')
print(response.status_code)
print(response.text)

response = requests.get('http://127.0.0.1:5000/tasks')
print(response.text)

response = requests.delete('http://127.0.0.1:5000/tasks/1')

response = requests.get('http://127.0.0.1:5000/tasks')
print(response.text)
