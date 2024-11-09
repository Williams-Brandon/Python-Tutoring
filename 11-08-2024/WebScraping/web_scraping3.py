from bs4 import BeautifulSoup
import requests

# URL of the CoinMarketCap homepage
url = "https://coinmarketcap.com/"

# Define headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Send an HTTP GET request to the URL with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Initialize a variable to store Bitcoin's price
bitcoin_price = None

# Find all table rows in the page
rows = soup.find_all('tr')

for row in rows:
    # Look for an 'a' tag with an href attribute that includes '/currencies/bitcoin/'
    a_tag = row.find('a', href=lambda href: href and '/currencies/bitcoin/' in href)
    if a_tag:
        # Once the Bitcoin row is found, find all 'td' elements in that row
        tds = row.find_all('td')
        
        # Ensure there are enough 'td' elements to extract the price
        if len(tds) >= 4:
            # The price is typically in the 4th 'td' element (index 3)
            price_td = tds[3]
            
            # Extract the text content and clean it up
            bitcoin_price = price_td.get_text(strip=True)
            break  # Exit the loop once Bitcoin's price is found

# Print the result
if bitcoin_price:
    print(f"The current price of Bitcoin is: {bitcoin_price}")
else:
    print("Bitcoin price not found.")
