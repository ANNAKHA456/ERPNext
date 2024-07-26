# # import requests

# # # URL to your Frappe site and endpoint
# # url = "http://demo01.com:8003/api/resource/Customer"
# # headers = {
# #     "Authorization": "token d1678c54ddcd0ca:2a06bfd2eeb8c0b",
# #     "Content-Type": "application/json"
# # }
# # data = {
# #     "customer_name":"John Doe",
# #     "customer_type": "Company",
# #     "phone_number":"8999999999"
# # }

# # # Make the API request
# # response = requests.put(url, headers=headers, json={"data": data})
# # print(response.json())
# import requests

# # URL to your Frappe site and endpoint for updating a Customer
# url = "http://demo01.com:8003/api/resource/Customer"
# headers = {
#     "Authorization": "token d1678c54ddcd0ca:2a06bfd2eeb8c0b",
#     "Content-Type": "application/json"
# }
# data = {
#     "customer_name": "John Doe",
#     "customer_type": "Company",
#     "phone_number": "8999999999"
# }

# try:
#     # Make the API request
#     response = requests.put(url, headers=headers, json=data)
    
#     # Check response status code
#     if response.status_code == 200:
#         print("Customer updated successfully")
#     else:
#         print(f"Failed to update customer. Status code: {response.status_code}")
#         print(response.text)  # Print the raw response content for debugging
# except Exception as e:
#     print(f"An error occurred: {str(e)}")
import requests

# URL to your Frappe site and endpoint for updating a Customer
url = "http://demo01.com:8003/api/resource/Customer"
headers = {
    "Authorization": "token d1678c54ddcd0ca:2a06bfd2eeb8c0b",
    "Content-Type": "application/json"
}
data = {
    "customer_name": "John Doe",
    "customer_type": "Company",
    "phone_number": "8999999999"
}

try:
    # Make the API request
    response = requests.post(url, headers=headers, json=data)
    
    # Check response status code
    if response.status_code == 200:
        print("Customer updated successfully")
    else:
        print(f"Failed to update customer. Status code: {response.status_code}")
        print(response.text)  # Print the raw response content for debugging
except Exception as e:
    print(f"An error occurred: {str(e)}")

