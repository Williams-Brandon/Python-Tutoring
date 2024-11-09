# Importing BeautifulSoup from the bs4 module and re for regular expressions (though not used in this code)
from bs4 import BeautifulSoup
import re

# Reading and parsing a local HTML file named 'index2.html'
with open("index2.html", "r") as f:  # Open 'index2.html' in read mode as 'f'
    doc = BeautifulSoup(f, "html.parser")  # Parse the file's content with BeautifulSoup using the 'html.parser'

# Finding all <input> tags with the attribute type="text"
tags = doc.find_all("input", type="text")  # Use find_all() to locate all <input> tags where type="text"

# Iterating over each found <input> tag and modifying its 'placeholder' attribute
for tag in tags:  # Loop through each <input> tag in the list
    tag['placeholder'] = "I changed you!"  # Set the 'placeholder' attribute to "I changed you!"

# Writing the modified HTML content back to a new file called 'changed.html'
with open("changed.html", "w") as file:  # Open 'changed.html' in write mode as 'file'
    file.write(str(doc))  # Convert the modified BeautifulSoup object back to a string and write it to the file
