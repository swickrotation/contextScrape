import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage to scrape
url = "https://en.m.wikipedia.org/wiki/Cinq_%C3%A0_sept"

# Define the key phrase
keyphrase = "English"

# Fetch the webpage content
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all paragraph tags
    paragraphs = soup.find_all("p")

    # Loop through paragraphs and print those containing the key phrase
    for paragraph in paragraphs:
        text = paragraph.get_text(strip=True)
        if re.search(keyphrase, text, re.IGNORECASE):
#            text = re.sub("\n", "", text)
            print(text)
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
