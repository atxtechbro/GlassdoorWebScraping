import json

import requests
from bs4 import BeautifulSoup

# Load existing industries or start with an empty dictionary
try:
    with open('industries.json', 'r') as f:
        industries = json.load(f)
except json.JSONDecodeError:
    industries = {}

# Load existing companies or start with an empty dictionary
try:
    with open('companies.json', 'r') as f:
        companies = json.load(f)
except json.JSONDecodeError:
    companies = {}

# Start URL
start_url = 'https://www.glassdoor.com/Reviews/index.htm?overall_rating_low=3.5&page='

# Iterate over pages
for page in range(1, 101):  # Adjust the range as needed
    response = requests.get(start_url + str(page))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Replace with your own logic to extract industries and companies
    new_industries = soup.find_all('div', class_='industry')
    new_companies = soup.find_all('div', class_='company')

    for industry in new_industries:
        industry_id = industry.get('id')
        industry_name = industry.get_text()

        # Add new industry to the dictionary if it's not already there
        if industry_id not in industries:
            industries[industry_id] = industry_name

    for company in new_companies:
        company_id = company.get('id')
        company_name = company.get_text()

        # Add new company to the dictionary if it's not already there
        if company_id not in companies:
            companies[company_id] = company_name

    # Save the updated industries back to the file
    with open('industries.json', 'w') as f:
        json.dump(industries, f, indent=2)

    # Save the updated companies back to the file
    with open('companies.json', 'w') as f:
        json.dump(companies, f, indent=2)
