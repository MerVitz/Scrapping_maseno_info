# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the Maseno University portal
url = "https://maseno.ac.ke/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract data from the landing page
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    paragraphs = soup.find_all('p')
    links = soup.find_all('a', href=True)
    list_items = soup.find_all(['li', 'ul', 'ol'])

    # Open a CSV file to write the data
    with open('maseno_university_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Type', 'Content'])

        # Write headings to the CSV file
        writer.writerow(['Headings'])
        for heading in headings:
            writer.writerow(['Heading', heading.text.strip()])

        # Write paragraphs to the CSV file
        writer.writerow(['Paragraphs'])
        for paragraph in paragraphs:
            writer.writerow(['Paragraph', paragraph.text.strip()])

        # Write list items to the CSV file
        writer.writerow(['List Items'])
        for item in list_items:
            writer.writerow(['List Item', item.text.strip()])

        # Write links to the CSV file
        writer.writerow(['Links'])
        for link in links:
            writer.writerow(['Link', f"{link.text.strip()} -> {link['href']}"])

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
