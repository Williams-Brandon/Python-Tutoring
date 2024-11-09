# Importing the required libraries: BeautifulSoup for HTML parsing and requests for making HTTP requests
from bs4 import BeautifulSoup
import requests

# URL of the website to scrape data from
url = "https://coinmarketcap.com/"

# Sending an HTTP GET request to the URL and getting the HTML content as text
result = requests.get(url).text  # The `.text` attribute extracts the response content as a string

# Parsing the HTML content with BeautifulSoup using the 'html.parser' parser
doc = BeautifulSoup(result, "html.parser")

# Accessing the <tbody> element that contains the table data for cryptocurrencies
tbody = doc.tbody  # Directly accesses the first <tbody> element in the document

# Getting all child elements (rows) within the <tbody>
trs = tbody.contents  # `contents` returns a list of all immediate children (typically <tr> elements)

# Initializing an empty dictionary to store cryptocurrency names and their corresponding prices
prices = {}

# Iterating over the first 10 rows (<tr> elements) in the table body
for tr in trs[:10]:  # Slice notation `[:10]` ensures only the first 10 rows are processed
    # Extracting the 3rd and 4th child elements (<td> elements) from each <tr>
    name, price = tr.contents[2:4]  # Unpacks the 3rd and 4th elements (name and price columns)

    # Extracting the text content from the <p> tag within the 'name' <td> element
    fixed_name = name.p.string  # Retrieves the string directly from the <p> tag containing the cryptocurrency name

    # Extracting the text content from the <a> tag within the 'price' <td> element
    fixed_price = price.a.string  # Retrieves the string directly from the <a> tag containing the price

    # Adding the name and price to the dictionary
    prices[fixed_name] = fixed_price  # Sets the cryptocurrency name as the key and its price as the value

# Printing the dictionary containing the names and prices of the top 10 cryptocurrencies
print(prices)
