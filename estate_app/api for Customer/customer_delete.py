import requests

# Replace with your actual ERPNext site URL and API endpoint
url = "http://demo01.com:8003/api/resource/Customer/sss"
headers = {
    "Authorization": "token d1678c54ddcd0ca:2a06bfd2eeb8c0b",
    "Content-Type": "application/json"
}

try:
    # Make the DELETE request
    response = requests.delete(url, headers=headers)
    
    # Check response status code
    if response.status_code == 200:
        print(f"Customer 'sss' deleted successfully")
    else:
        print(f"Failed to delete customer 'sss'. Status code: {response.status_code}")
        print(response.text)  # Print the raw response content for debugging
except Exception as e:
    print(f"An error occurred: {str(e)}")
