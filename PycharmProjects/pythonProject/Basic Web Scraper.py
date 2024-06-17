import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "http://quotes.toscrape.com/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all quote elements on the page
    quotes = soup.find_all('div', class_='quote')

    # Iterate through each quote element and extract text and author
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f"Quote: {text}\nAuthor: {author}\n")
else:
    print("Failed to retrieve the webpage.")
