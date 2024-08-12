import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://www.presidency.ucsb.edu/documents/statement-signing-the-promoting-resolution-the-tibet-china-dispute-act"

# Send a GET request to the webpage
response = requests.get(url)
encoding = response.apparent_encoding
response.encoding = encoding
bd_soup = BeautifulSoup(response.text,"lxml")
pretty_html = bd_soup.prettify()

with open('parsed_content_373505.html', 'w', encoding='utf-8') as file:
    file.write(pretty_html)

print("HTML content has been written to parsed_content.txt")