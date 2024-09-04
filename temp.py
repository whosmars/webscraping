import requests

# Send a GET request to the URL

response = requests.get('https://www.hostinger.com/tutorials/how-to-run-a-python-script-in-linux')

# Print the HTML content of the page

print(response.text)
