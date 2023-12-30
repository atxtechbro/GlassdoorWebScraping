import csv
import itertools
import json
import logging
import random
import string
import time

import requests

logging.basicConfig(level=logging.INFO)

url = 'https://www.glassdoor.com/graph'
headers = {
    'authority': 'www.glassdoor.com',
    'method': 'POST',
    'path': '/graph',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'apollographql-client-name': 'company.explorer',
    'apollographql-client-version': '3.18.12',
    'content-length': '1656',
    'content-type': 'application/json',
    'cookie': 'asst=1703884286.0; gdId=d9f49a39-3a83-4254-9b05-ee508425e1fb; GSESSIONID=undefined; JSESSIONID=8BD9728688F35A560BE14C52BF9086B9; cass=1; companiesClicked=true; AWSALB=a2RFma+/tBhq9j3ija3daoNCuK1UH8HKQd7nivlpngGq5V31uV9XXlHARG405MIDvWKrW8xoY9GyzGxzJPJfU3+lpqqvOvIKKZ6GiAmJcc3TnSW1DDP0q9+7n8Fc; AWSALBCORS=a2RFma+/tBhq9j3ija3daoNCuK1UH8HKQd7nivlpngGq5V31uV9XXlHARG405MIDvWKrW8xoY9GyzGxzJPJfU3+lpqqvOvIKKZ6GiAmJcc3TnSW1DDP0q9+7n8Fc; gdsid=1703884287447:1703887414513:69AF0D0737F607A97F0296018DAD700E; __cf_bm=7ojqBHf.3Na.L6AoKxk6Rk4PkfZ5tXzSp7Vd0C_nrs0-1703887414-1-AR44LMU/L9o7qFj5QfVhf1Nr3q/83wdIFwM0amtWv+1P/C9zHqJLZBoDYp9Vjwp4cUl1pnUX2WIot7YrLAaz9nQTkXd1pPp6Zl2XCFoq9AVr; _cfuvid=ArL2v6Qdq7.cGjhG5waoyDU8c1BitOizDPildIZEHGA-1703887414645-0-604800000',
    'gd-csrf-token': 'W4qI4GJFkb3rDWO0KbLjUw:EF2AITEIXWTdlvXJRskcgzt6C-uTRWH4WurHQRk4o4bpFUMmBcxsLiAoe_qNjrulIqPKZF7-DI9rBQ644Vn2cA:JVJdlO9md9osN-m0WbtgFcqEyi1ScjPDjD2siKH1-_k',
    'origin': 'https://www.glassdoor.com',
    'referer': 'https://www.glassdoor.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}


# List of search strings
search_strings = list(string.ascii_lowercase) + ['']
random.shuffle(search_strings)

# Set of visited companies
visited = set()

for employer_name, job_title in itertools.product(search_strings, repeat=2):
    logging.info(f"Searching for employer_name {employer_name}* and job_title {job_title}*")
    # Your GraphQL query
    graphql_query = {
        "operationName": "AllResultsCompanySearch",
        "variables": {
            "context": {"domain": "glassdoor.com"},
            "employerName": employer_name,
            "jobTitle": job_title,
            "locationId": 1,
            "locationType": "",
            "numPerPage": 18
        },
        "query": """
            query AllResultsCompanySearch(
                $jobTitle: String,
                $employerName: String,
                $locationId: Int,
                $locationType: String,
                $numPerPage: Int,
                $context: Context
            ) {
                employerNameCompaniesData: employerSearch(
                    employerName: $employerName
                    location: {locationId: $locationId, locationType: $locationType}
                    numPerPage: $numPerPage
                    context: $context
                    sortOrder: MOSTRELEVANT
                ) {
                    ...CompanySearchResult
                    __typename
                }
                directHitCompany: employerSearch(
                    filterDirectHit: true
                    employerName: $employerName
                    location: {locationId: $locationId, locationType: $locationType}
                    context: $context
                    sortOrder: MOSTRELEVANT
                ) {
                    ...CompanySearchResult
                    __typename
                }
                jobTitleCompaniesData: employerSearch(
                    jobTitle: $jobTitle
                    location: {locationId: $locationId, locationType: $locationType}
                    numPerPage: $numPerPage
                    context: $context
                    sortOrder: MOSTRELEVANT
                ) {
                    ...CompanySearchResult
                    __typename
                }
            }

            fragment CompanySearchResult on UgcSearchV2EmployerResult {
                employer {
                    id
                    shortName
                    squareLogoUrl
                    headquarters
                    size
                    sizeCategory
                    overview {
                        description
                        __typename
                    }
                    primaryIndustry {
                        industryId
                        industryName
                        __typename
                    }
                    links {
                        overviewUrl
                        __typename
                    }
                    counts {
                        reviewCount
                        salaryCount
                        globalJobCount {
                            jobCount
                            __typename
                        }
                        __typename
                    }
                    __typename
                }
                employerRatings {
                    overallRating
                    __typename
                }
                __typename
            }
        """
    }

    response = requests.post(url, headers=headers, data=json.dumps(graphql_query))
    data = response.json()

    # Add the data to company_data.csv
    with open('company_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for result in data['data']['employerNameCompaniesData']:
            company = result['employer']
            logging.info(f"Adding company: {company['shortName']}")
            time.sleep(1)
            if company['id'] in visited:
                continue
            writer.writerow([
                company['id'],
                company['shortName'],
                company['squareLogoUrl'],
                company['headquarters'],
                company['size'],
                company['sizeCategory'],
                company['overview']['description'],
                company['primaryIndustry']['industryId'],
                company['primaryIndustry']['industryName'],
                company['links']['overviewUrl'],
                company['counts']['reviewCount'],
                company['counts']['salaryCount'],
                company['counts']['globalJobCount']['jobCount'],
                result['employerRatings']['overallRating']
            ])
            visited.add(company['id'])
