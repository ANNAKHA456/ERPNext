import requests

# URL to your Frappe site and endpoint
url = "http://demo01.com:8003/api/method/estate_app.estate_plan.api.teacher_details_new_crud.update_teacher"
headers = {
    "Authorization": "token d1678c54ddcd0ca:2a06bfd2eeb8c0b",
    "Content-Type": "application/json"
}
data = {
    "teacher_id": "T001",
    "name": "Jane Smith"  # Updating the name field
}

# Make the API request
response = requests.put(url, headers=headers, json=data)
print(response.json())