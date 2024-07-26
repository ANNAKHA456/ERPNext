import requests

# URL to your Frappe site and endpoint
url = "http://demo01.com:8003/api/resource/Customer"
headers = {
    "Authorization": "token d1678c54ddcd0ca:2a06bfd2eeb8c0b",
    "Content-Type": "application/json"
}
data = {
    "customer_name": "John Doe",
    "customer_type": "Individual",
    }

# Make the API request
response = requests.post(url, headers=headers, json={"data": data})
print(response.json())