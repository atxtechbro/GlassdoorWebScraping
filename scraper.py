import json

import requests

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

# Your GraphQL query
graphql_query = {
    "operationName": "FeaturedJobsQuery",
    "variables": {
        "keyword": "",
        "locationType": "COUNTRY",
        "locationId": 1,
        "adSlotName": "search-reviews-lf-right",
        "numPerPage": 5
    },
    "query": "query FeaturedJobsQuery($keyword: String!, $locationType: LocationTypeEnum, $locationId: Int!, $adSlotName: String!, $numPerPage: Int!) { jobListings(contextHolder: {adSlotName: $adSlotName, searchParams: {numPerPage: $numPerPage, searchType: FJ, skipFeaturedJobs: true, skipUrgencyLabel: true, locationType: $locationType, locationId: $locationId, keyword: $keyword}}) { jobListings { jobview { job { listingId __typename } overview { id name: shortName squareLogoUrl(size: SMALL) __typename } rating { starRating __typename } header { ageInDays jobLink jobTitleText locationName payCurrency payPeriod payPercentile10 payPercentile90 salarySource __typename } __typename } __typename } __typename } }"
}

response = requests.post(url, headers=headers, data=json.dumps(graphql_query))

print(response.text)
