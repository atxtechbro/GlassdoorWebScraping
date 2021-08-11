import json
import os
import pickle
import requests


def bizBookLoad():
    global bizBook, loadedLength 
    f = open('bizBook.txt', 'rb')
    bizBook = pickle.load(f)
    f.close()
    loadedLength = len(bizBook)

    
def bizBookSave():
    global checkDiffI
    """for maintainability, see last line of code which uses a different object to
    calculate what SHOULD be a matching difference or else program should fail as it isn't
    working properly. Intend to leave this assertion safeguard in for now and will
    remove it after further testing down the road. cost free safety check"""
    f = open('bizBook.txt', 'wb')
    pickle.dump(bizBook, f)
    path = os.getcwd()
    storageLocation = (path + f.name)
    savedLength = len(bizBook)
    f.close()
    checkDiffI = savedLength - loadedLength
    print(checkDiffI, 'new records saved to', storageLocation)
    


bizBookLoad()
#static parts of url (Head & Tail) will never change
head = 'https://www.glassdoor.com/seo/ajax/ugcSearch.htm?minRating=0&maxRating=5&'
tail = '&domain=glassdoor.com&surgeHiring=false'

def requestRecords(qtyPerPage, startPageSelected):
    global JSON
    cursor = f'numPerPage={qtyPerPage}&pageRequested={startPageSelected}'
    url = head+cursor+tail #stitching the pieces together

    
    #avoid getting red flagged
    headers = {'User-Agent': 'Mozilla/5.0'} #vs {'User-Agent': 'python-requests/2.26.0'}
    r = requests.get(url, headers=headers)
    assert r.status_code == 200
    
    
    #refine data further by accessing key 'results' and subKey 'employerSearchResponse'
    JSON = json.loads(r.text)
    #reaching a point where we have the 100 records requested in the numPerPage url parameter
    records = JSON['employerSearchResponse']['results']
    try:
        assert qtyPerPage == len(records)
    except AssertionError:
        print('requested records:', qty)
        print('records available per request:', len(records))
        print('for requestRecords(qty), try lowering qty to <= len(records)')
        raise
        
        
    before = len(bizBook)
    scannedRecords = {}
    for rec in records:
        corporateID, corporateName = rec['id'], rec['name']
        scannedRecords[corporateID] = corporateName
        
        
    newEntries = { k : scannedRecords[k] for k in set(scannedRecords) - set(bizBook) }
    checkDiffTwo = len(newEntries)
    bizBook.update(scannedRecords)
    bizBookSave()
    
    
    num, den = JSON['pageRequested'], JSON['employerSearchResponse']['numPagesAvailable']
    progress = num/den
    progress = '{:.3%}'.format(progress).replace('%', ' %')
    print(progress, '{key: value}', 'pairs scraped and saved')
    assert checkDiffI == checkDiffI
    return newEntries

requestRecords(qtyPerPage=100, startPageSelected=25)

#sample output
"""
78 new records saved to /home/<USER NAME>/ScrapingChallenge/venv/binbizBook.txt
0.459 % {key: value} pairs scraped and saved

{343552: 'Egencia',
 512004: 'Cooper’s Hawk Winery & Restaurants ',
 4612: 'Hines Interests Limited Partnership',
 35336: 'Virgin America Inc.',
 3083: 'Baker Botts L.L.P.',
 1038: 'TOTAL S.A.',
 530: 'PVH Corp.',
 35347: 'City Furniture, Inc.',
 424981: 'FHI 360',
 28187: 'Capgemini Engineering',
 453680: 'C Spire Wireless',
 24625: 'Ball State University',
 4662: 'Methodist Le Bonheur Healthcare',
 14905: 'Bell Helicopter Textron Inc.',
 19534: 'Simpson Manufacturing Co., Inc.',
 16462: 'Consolidated Edison Company of New York, Inc.',
 315986: 'Sheraton Hotels & Resorts',
 1624: 'Maxim Integrated Products, Inc.',
 279137: 'Remington Hotels Corporation',
 19561: 'Kettering Health Network',
 11902: 'Chevron Phillips Chemical Company LLC',
 1317005: 'Siemens Healthcare GmbH',
 238741: 'GEP formerly Global eProcure',
 17045: 'The ICW Group',
 670: 'The Toro Company',
 920736: 'himagine solutions inc',
 10918: 'CEMEX, S.A.B. de C.V.',
 18601: "Nationwide Children's Hospital Inc.",
 8879: 'Billabong International Limited',
 249007: 'Baker Tilly International',
 236210: 'Endurance International Group',
 671930: 'Laser Away',
 19132: "Children's Mercy Hospitals and Clinics",
 300225: 'Varonis Systems, Inc.',
 22726: 'The Corcoran Group, Inc.',
 26827: 'ProQuest LLC',
 629964: 'Aspect Education UK Ltd.',
 17102: 'Benchmark Hospitality International',
 664796: 'Bryan Health Systems',
 15078: 'Firmenich SA',
 7917: 'Ariba, Inc.',
 15096: 'Wynn Resorts, Limited',
 25850: 'Helix Electric, Inc.',
 28411: 'The Lockton Companies, LLC',
 1771815: 'Relativity ODA LLC',
 20782: 'Tumi, Inc',
 39220: 'NxStage Medical, Inc.',
 299317: 'Clinique',
 11574: 'OpenTable, Inc.',
 2868: 'L.L. Bean, Inc.',
 273214: 'Popular Tech',
 15177: 'Kimley-Horn and Associates, Inc.',
 363347: 'Berkadia Commercial Mortgage',
 41300: 'Bureau of Reclamation',
 14173: 'AREVA',
 20320: 'Altair Engineering Inc.',
 101738: 'Imperva, Inc.',
 122233: 'Hahnemann University Hospital',
 582526: 'Zurich Insurance',
 295294: 'Samsung Research America',
 200070: 'De Lage Landen',
 20875: 'Phoebe Putney Memorial Hospital',
 372107: 'Otter Products, LLC',
 212879: 'Trilogy Health Services LLC',
 31120: 'Cherry Bekaert LLP',
 129950: 'Montgomery College',
 1969055: 'Maxar Technologies Ltd. ',
 4512: 'APAC Customer Services Inc.',
 259493: 'Impetus Technologies',
 14252: 'The Depository Trust & Clearing Corporation',
 6060: 'TPG Capital, L.P.',
 1685428: 'Essity',
 41913: 'New York State Unified Court System',
 16834: 'Holder Construction Company',
 13762: 'Oaktree Capital Group, LLC',
 13273: 'Paramount Pictures Corporation',
 4075: 'Orange',
 3060: 'Akin Gump Strauss Hauer & Feld LLP'}
 """
