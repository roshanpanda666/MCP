import requests

# POST
todo = {
    "house": "001",
    "price": "20000",
    "year": "2002",
    "area":"bhubaneshwar"
}
response = requests.post("http://127.0.0.1:8000/", json=todo)
print(response.json())

# GET
response = requests.get("http://127.0.0.1:8000/")
print(response.json())