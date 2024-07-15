import requests

response  =  requests.post("http://127.0.0.1:5000/cars")

expected = 'creating new car'
actual =response.text
assert expected == actual

expected =  201
actual =  response.status_code
assert expected == actual

print(response.text)