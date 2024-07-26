import requests

# URL to your Frappe site and endpoint
url = "http://demo01.com:8003/api/method/estate_app.estate_plan.api.teacher_details_new_crud.read_all_teachers"
headers = {
    "Authorization": "token d1678c54ddcd0ca:2a06bfd2eeb8c0b",
    "Content-Type": "application/json"
}
response = requests.get(url, headers=headers)
print(response.json())