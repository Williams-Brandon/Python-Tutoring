# Importing required libraries
from bs4 import BeautifulSoup  # Used for parsing and navigating HTML content
import requests  # Used for making HTTP requests to retrieve web content
import re  # Regular expressions library for pattern matching in text

# Taking user input for the product search term
search_term = input("What product do you want to search for? ")

# Constructing the URL for the search query
url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
page = requests.get(url).text  # Sends a GET request to the URL and extracts the content as text
doc = BeautifulSoup(page, "html.parser")  # Parses the HTML content using BeautifulSoup

# Finding the pagination information (if it exists)
try:
    page_text = doc.find(class_="list-tool-pagination-text").strong
    pages = int(page_text.text.split("/")[-1].strip())  # Extracts the total number of pages as an integer
except AttributeError:
    pages = 1  # If pagination element is not found, set to 1

# Dictionary to store found items with details
items_found = {}

# Looping through each page of search results
for page in range(1, pages + 1):
    url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
    page_content = requests.get(url).text
    doc = BeautifulSoup(page_content, "html.parser")

    # Finding the container with all item listings
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    if not div:
        continue  # Skip if the container is not found

    # Finding all items that match the search term
    items = div.find_all("div", class_="item-container")
    for item in items:
        # Extracting the item name
        name_tag = item.find("a", class_="item-title")
        if not name_tag:
            continue
        name = name_tag.text

        # Extracting the item price
        price_tag = item.find(class_="price-current")
        if not price_tag or not price_tag.find("strong"):
            continue
        price = price_tag.find("strong").text.replace(",", "")

        # Extracting the item link
        link = name_tag['href']

        # Adding item details to the dictionary
        items_found[name] = {"price": int(price), "link": link}

# Sorting the items found by price in ascending order
sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

# Printing out the sorted items with their details
for item in sorted_items:
    print(item[0])  # Prints the name of the item
    print(f"${item[1]['price']}")  # Prints the price of the item
    print(item[1]['link'])  # Prints the URL of the item
    print("-------------------------------")  # Prints a separator line for readability
