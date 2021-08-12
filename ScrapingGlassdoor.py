import json
import random
import requests
import time

bizBook = {}
pageNumber = 95
sectorBase = 10000
sectorIndex = sectorBase + 1

print('page number initialized to ', pageNumber)

with open('bizBook.json', 'w') as f:
    f.write(json.dumps(bizBook))
with open('bizBook.json', 'r') as f:
    businesses = f.read()
    bizBook = json.loads(businesses) 
with open('industries.json', 'r') as f:
    sectors_ = f.read()
    sectors = json.loads(sectors_)
    
    
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
    }  
    
sectorList = []
for key in sectors.keys():
    sectorList.append(key)

while True:   
    startUrl = f'https://www.glassdoor.com/seo/ajax/ugcSearch.htm?minRating=0&maxRating=5&numPerPage=100&'

    if pageNumber >= 100:
        pageNumber = 1
        sectorIndex += 1
    else:
        pageNumber += 1
        pass
    urlAppendage = f'pageRequested={pageNumber}&domain=glassdoor.com&surgeHiring=false&sectorIds={sectorIndex}'
    url = startUrl + urlAppendage
     
      
    r = requests.get(url, headers=headers) #avoid getting red flagged
    jsonResponse = json.loads(r.text)
    
    if pageNumber > jsonResponse['employerSearchResponse']['numPagesAvailable']:
        sectorIndex += 1
        pageNumber = 1
        urlAppendage = f'pageRequested={pageNumber}&domain=glassdoor.com&surgeHiring=false&sectorIds={sectorIndex}'
        url = startUrl + urlAppendage
        r = requests.get(url, headers=headers) #avoid getting red flagged
        jsonResponse = json.loads(r.text)
    else:
        pass
    
    records = jsonResponse['employerSearchResponse']['results']
    #now all our data in contained in records which are 100 mini dictionaries
    
    #extracting the exact corporateID, corporateName from each of the 100 records and saving them to a scannedRecords dictionary which will end up containing all of them
    beforeBizBookLength = len(bizBook)
    for rec in records:
        corporateID, corporateName = rec['id'], rec['name']
        bizBook[corporateID] = corporateName
    afterBizBookLength = len(bizBook)
    collectedPairsThisPage = afterBizBookLength - beforeBizBookLength

    print('p.', pageNumber, sectors[f'{sectorIndex}'], f'(+{collectedPairsThisPage})')
    
    with open('bizBook.json', 'w') as f:
        f.write(json.dumps(bizBook, indent = 2))
    time.sleep(random.randint(4,5))
