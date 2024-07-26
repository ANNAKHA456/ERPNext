# # import requests
# # from requests.auth import HTTPBasicAuth

# # # Your ERPNext/Frappe instance URL
# # base_url = "https://demo01.com:8003"

# # # Your API key and secret
# # api_key = "d1678c54ddcd0ca"
# # api_secret = "0d5add893901d51"

# # # File to upload
# # file_path = "/home/anakha/frappe-bench03/apps/estate_app/estate_app/api_files/upload.txt"

# # # API endpoint to upload file
# # upload_url = f"{base_url}/api/method/upload_file"

# # # Read the file content
# # with open(file_path, 'rb') as file:
# #     # Prepare the request
# #     files = {
# #         'file': file,
# #         'is_private': (None, '1'),  # Set to '0' if the file should be public
# #     }
# #     headers = {
# #         'Authorization': HTTPBasicAuth(api_key, api_secret),
# #     }

# #     # Send the request
# #     response = requests.post(upload_url, files=files, auth=HTTPBasicAuth(api_key, api_secret))

# # # Check the response
# # if response.status_code == 200:
# #     print("File uploaded successfully")
# #     print("Response:", response.json())
# # else:
# #     print("Failed to upload file")
# #     print("Response:", response.text)
# import requests
# from requests.auth import HTTPBasicAuth

# # Your ERPNext/Frappe instance URL
# base_url = "http://demo01.com:8003"

# # Your API key and secret
# api_key = "d1678c54ddcd0ca"
# api_secret = "0d5add893901d51"

# # File to upload
# file_path = "/home/anakha/frappe-bench03/apps/estate_app/estate_app/api_files/upload.txt"

# # API endpoint to upload file
# upload_url = f"{base_url}/api/method/upload_file"

# # Read the file content
# with open(file_path, 'rb') as file:
#     # Prepare the request
#     files = {
#         'file': file,
#         'is_private': (None, '1'),  # Set to '0' if the file should be public
#     }
    
#     # Send the request with SSL verification disabled (for testing purposes)
#     try:
#         response = requests.post(upload_url, files=files, auth=HTTPBasicAuth(api_key, api_secret), verify=False)
        
#         # Check the response
#         if response.status_code == 200:
#             print("File uploaded successfully")
#             print("Response:", response.json())
#         else:
#             print("Failed to upload file")
#             print("Response:", response.text)
#     except requests.exceptions.RequestException as e:
#         print("An error occurred:", e)

# import requests
# import base64

# # Convert image to base64 (if needed)
# def convert_image_to_base64(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode()

# # Upload image to ERPNext
# def upload_image(image_path, image_name, session):
#     url = "http://demo01.com:8003/api/method/upload_file"
#     files = {
#         'file': (image_name, open(image_path, 'rb')),
#         'is_private': '1',
#         'docname': 'Employee'
#     }
#     response = session.post(url, files=files)
#     return response.json()

# # Update Employee with image URL
# def update_employee_with_image(employee_name, file_url, session):
#     data = {
#         'image': file_url
#     }
#     response = session.put(f"http://demo01.com:8003/api/resource/Employee/{employee_name}", json=data)
#     return response.json()

# # Main logic
# session = requests.Session()
# session.headers.update({
#     'Authorization': 'token d1678c54ddcd0ca:0d5add893901d51',
#     'Content-Type': 'application/json'
# })

# image_path = '/home/anakha/frappe-bench03/apps/estate_app/estate_app/api_files/download.jpeg'
# employee_name = 'EMP/0001'
# image_name = 'download.jpeg'

# upload_response = upload_image(image_path, image_name, session)
# file_url = upload_response['message']['file_url']

# update_response = update_employee_with_image(employee_name, file_url, session)
# print(update_response)


import requests
import base64

# Convert image to base64 (if needed)
def convert_image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        print("File not found.")
        return None

# Upload image to ERPNext
def upload_image(image_path, image_name, session):
    url = "http://demo01.com:8003/api/method/upload_files"
    try:
        with open(image_path, 'rb') as image_file:
            files = {
                'file': (image_name, image_file),
                'is_private': '1',
                'docname': 'Employee'
            }
            response = session.post(url, files=files)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"Error uploading image: {e}")
        return None

# Update Employee with image URL
def update_employee_with_image(first_name, file_url, session):
    data = {
        'Image': file_url
    }
    try:
        response = session.put(f"http://demo01.com:8003/api/resource/Employee/{first_name}", json=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error updating employee: {e}")
        return None

# Main logic
session = requests.Session()
session.headers.update({
    'Authorization': 'token d1678c54ddcd0ca:0d5add893901d51',
    'Content-Type': 'application/json'
})

image_path = '/home/anakha/frappe-bench03/apps/estate_app/estate_app/api_files/download.jpeg'
first_name = 'Anna'
image_name = 'download.jpeg'

# Convert image to base64 if needed
image_base64 = convert_image_to_base64(image_path)

if image_base64:
    # Upload the image
    upload_response = upload_image(image_path, image_name, session)
    
    if upload_response and 'message' in upload_response:
        file_url = upload_response['message']['file_url']
        
        # Update employee with image URL
        update_response = update_employee_with_image(first_name, file_url, session)
        print(update_response)
    else:
        print("Failed to upload image.")
else:
    print("Image conversion to base64 failed.")
