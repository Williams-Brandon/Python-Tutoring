# Importing the BeautifulSoup library from the bs4 module and the requests library
from bs4 import BeautifulSoup
import requests

# Reading and parsing a local HTML file
with open("index.html", "r") as f:  # Open 'index.html' in read mode as 'f'
    doc = BeautifulSoup(f, "html.parser")  # Parse the file content using BeautifulSoup and store it in 'doc'

# Finding the first <p> tag in the parsed document
tags = doc.find_all("p")[0]  # Find all <p> tags and select the first one (index 0)

# Finding all <b> tags within the first <p> tag
print(tags.find_all("b"))  # Print a list of all <b> tags nested inside the first <p> tag

# Accessing an HTML page from a website using requests
url = "https://www.newegg.com/zotac-amp-zt-d40820f-10p-nvidia-geforce-rtx-4080-super-16gb-gddr6x/p/N82E16814500583"

# Sending a GET request to the specified URL and storing the response
result = requests.get(url)  # Use requests to get the content of the webpage
doc = BeautifulSoup(result.text, "html.parser")  # Parse the HTML content using BeautifulSoup and store it in 'doc'

# Finding all text nodes in the document that contain the "$" character (indicating prices)
prices = doc.find_all(text="$")  # Find all text nodes that include "$"

# Getting the parent element of the first occurrence of a text node containing "$"
parent = prices[0].parent  # Access the parent element of the first "$" found

# Finding the <strong> tag within that parent element, typically where the actual price might be
strong = parent.find("strong")  # Search for a <strong> tag within the parent element

# Printing the string content of the <strong> tag (the price)
print(f"The price is {strong.string} dollars")  # Print the text contained within the <strong> tag
