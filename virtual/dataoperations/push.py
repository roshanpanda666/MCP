import requests

# POST
todo = {
    "house": "001",
    "price1": "30200",
    "price2": "50060",
    "price3": "70400",
    "year1": "2008",
    "year2": "2009",
    "year3": "2010",
    "area":"bhubaneshwar"
}
response = requests.post("http://127.0.0.1:8000/", json=todo)
print(response.json())

# GET
response = requests.get("http://127.0.0.1:8000/")
print(response.json())