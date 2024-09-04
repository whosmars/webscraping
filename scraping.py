import requests

from bs4 import BeautifulSoup

# Send a GET request to the URL

response = requests.get('https://link')

# Parse the HTML content using BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with a specific tag (e.g. all h2 headings)

titles = soup.find_all('h2')

# Extract text content from each H2 element

for title in titles:

	print(title.text)
