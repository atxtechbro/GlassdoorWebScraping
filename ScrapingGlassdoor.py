import json
import requests

def load():
    global bizBook
    
    with open('BizBook.json', 'r') as f:
        data = f.read()
        bizBook = json.loads(data)
    f.close()
    return bizBook
load() 


def requestRecords():
    pageNumber = round(len(bizBook) / 100)
    url = f'https://www.glassdoor.com/seo/ajax/ugcSearch.htm?minRating=0&maxRating=5&numPerPage=100&pageRequested={pageNumber}&domain=glassdoor.com&surgeHiring=false'

    
    #avoid getting red flagged
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}) #vs {'User-Agent': 'python-requests/2.26.0'}
    assert r.status_code == 200
    
    
    #refine data further by accessing key 'results' and subKey 'employerSearchResponse'
    JSON = json.loads(r.text)
    #reaching a point where we have the 100 records requested in the numPerPage url parameter
    records = JSON['employerSearchResponse']['results']
        
    before = len(bizBook)
    scannedRecords = {}
    for rec in records:
        corporateID, corporateName = rec['id'], rec['name']
        scannedRecords[corporateID] = corporateName
        
        
    newEntries = { k : scannedRecords[k] for k in set(scannedRecords) - set(bizBook) }
    bizBook.update(scannedRecords)
    save()
    
    
    pctProg = len(bizBook) / JSON['employerSearchResponse']['numRecordsAvailable']
    pctProg = '{:.4%}'.format(pctProg).replace('%', ' %')
    print(pctProg, '{key: value}', 'pairs scraped and saved')
    print(len(newEntries))
    print(newEntries)

    
def save():
    with open('BizBook.json', 'w') as f:
        f.write(json.dumps(bizBook, indent = 2))
    f.close()
    
requestRecords()
