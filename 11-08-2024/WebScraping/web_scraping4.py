# Importing required libraries
import requests  # Helps us download the webpage
from bs4 import BeautifulSoup  # Helps us read and parse the webpage

# Step 1: Ask the user what product they want to search for
search_term = input("What product do you want to search for on Newegg? ")

# Step 2: Create the search URL
# Newegg's search URL looks like this: https://www.newegg.com/p/pl?d=SEARCH_TERM
# We'll replace SEARCH_TERM with what the user entered
url = f"https://www.newegg.com/p/pl?d={search_term}"

# Step 3: Download the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to retrieve the webpage.")
    exit()

# Step 4: Parse the webpage content
soup = BeautifulSoup(response.text, "html.parser")

# Step 5: Find all products on the page
# Newegg lists products in 'div' tags with the class 'item-cell'
products = soup.find_all('div', class_='item-cell')

# Check if any products were found
if not products:
    print("No products found.")
    exit()

# Step 6: Loop through the products and get their names and prices
print(f"\nProducts found for '{search_term}':\n")

for product in products:
    # Find the product name
    name_tag = product.find('a', class_='item-title')
    if name_tag:
        product_name = name_tag.text
    else:
        product_name = "No name found"

    # Find the product price
    price_tag = product.find('li', class_='price-current')
    if price_tag:
        # The price is split into strong (dollars) and sup (cents)
        dollars = price_tag.find('strong')
        cents = price_tag.find('sup')
        if dollars and cents:
            product_price = f"${dollars.text}{cents.text}"
        elif dollars:
            product_price = f"${dollars.text}"
        else:
            product_price = "Price not available"
    else:
        product_price = "Price not available"

    # Print the product name and price
    print(f"Name: {product_name}")
    print(f"Price: {product_price}")
    print("-" * 40)  # Prints a line to separate products
