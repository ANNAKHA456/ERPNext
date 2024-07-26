import requests

# URL to your Frappe site and endpoint
url = "http://demo01.com:8003/api/resource/Customer"
headers = {
    "Authorization": "token d1678c54ddcd0ca:2a06bfd2eeb8c0b",
    "Content-Type": "application/json"
}
params = {
    "fields": ["name", "customer_name", "customer_type", "territory"]
}

response = requests.get(url, headers=headers)
print(response.json())