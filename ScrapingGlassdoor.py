import json
import random
import requests
import time
bizBook = {}
pageNumber = 1
#create bizBook file and initiate pageNumber to 1
with open('BizBook.json', 'w') as f:
    f.write(json.dumps(bizBook))

while True:
    
    with open('BizBook.json', 'r') as f:
        businesses = f.read()
        bizBook = json.loads(businesses)

    url = f'https://www.glassdoor.com/seo/ajax/ugcSearch.htm?minRating=0&maxRating=5&numPerPage=100&pageRequested={pageNumber}&domain=glassdoor.com&surgeHiring=false'
    pageNumber += 1

    
    #avoid getting red flagged
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}) #vs {'User-Agent': 'python-requests/2.26.0'}
    assert r.status_code == 200
    
    
    jsonResponse = json.loads(r.text)
    records = jsonResponse['employerSearchResponse']['results']
    #now all our data in contained in records which are 100 mini dictionaries
    
    #extracting the exact corporateID, corporateName from each of the 100 records and saving them to a scannedRecords dictionary which will end up containing all of them
    scannedRecords = {}
    for rec in records:
        corporateID, corporateName = rec['id'], rec['name']
        scannedRecords[corporateID] = corporateName
        bizBook.update(scannedRecords) #add new data to our bizBook and save it to local storage
    with open('BizBook.json', 'w') as f:
        f.write(json.dumps(bizBook, indent = 2))
    
    #scraping progress statistics
    mileMarker = len(bizBook)
    destination = jsonResponse['employerSearchResponse']['numRecordsAvailable']
    percentageComplete = mileMarker / destination
    pctProg = '{:.4%}'.format(percentageComplete) #percentage of scraped companies
    print(pctProg, str(mileMarker) + ' / ' + str(destination))
    time.sleep(random.randint(5,10))
