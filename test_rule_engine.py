import requests


def test_create_rule():
    url = "http://localhost:5000/create_rule"
    rule_string = "age > 30 AND department = 'Sales'"
    response = requests.post(url, json={"rule_string": rule_string})
    print(response.json())


test_create_rule()
