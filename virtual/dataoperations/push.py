import requests

# POST
todo = {
    "house": "001",
    "price1": "20200",
    "price2": "30060",
    "price3": "40400",
    "year1": "2005",
    "year2": "2006",
    "year3": "2007",
    "area":"bhubaneshwar"
}
response = requests.post("http://127.0.0.1:8000/", json=todo)
print(response.json())

# GET
response = requests.get("http://127.0.0.1:8000/")
print(response.json())