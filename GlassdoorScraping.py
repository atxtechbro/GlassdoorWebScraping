#!/usr/bin/env python
# coding: utf-8

# In[19]:


from bs4 import BeautifulSoup
import json
import pickle
import re
import requests
import random
from time import sleep

'''
initializing the program
to start on page 1
'''

def getCleanerData():
    global refinedData, regex_response, pageNumber, indexNumber
    headers={'User-Agent': 'Mozilla/5.0'}
    
    #url = 'https://www.glassdoor.com/Job/us-jobs-SRCH_IL.0,2_IN{}_IP{}.htm'.format(indexNumber, pageNumber)
    url='https://www.glassdoor.com/Job/santa-clara-business-analyst-jobs-SRCH_IL.0,11_IC1147439_KO12,28_IP2.htm'
    print(url)
    print('index', indexNumber, 'page', pageNumber)
    
    if pageNumber>30:
        pageNumber=1
        indexNumber=+1
    else:
        pageNumber+=1
        
    r = requests.get(url, headers=headers)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    a = soup.findAll('script',{'type':'text/javascript'})
    regex = r'{\"bundle\".*'
    try:
        regex_response = re.search(regex, str(a)).group(0)
    except AttributeError:
        getCleanerData()
        
    data = json.loads(regex_response[:-1])
    refinedData = data['jlData']
    return pageNumber, indexNumber   
    
def bizBookSave():
    
    '''saves records to text file'''
    
    f = open('bizBook.txt', 'wb')
    pickle.dump(bizBook, f)
    f.close()
       
def bizBookLoad():
    global bizBook  
    f = open('bizBook.txt', 'rb')
    bizBook = pickle.load(f)
    f.close()

def getCities():
    refinedDataForCities = refinedData['serpSeoLinksVO']['topCityIdsToNameResults']
    for city in refinedDataForCities:
        cityID = city['key']
        cityName = city['value']
        try:
            cities.update({cityID: cityName})
        except NameError:
            cities = {}
            cities.update({cityID: cityName})
    return cities

def getCompanies():
    global bizBook
    for listing in refinedData['jobListings']:
        miniDict = listing['employer']
        for m in miniDict:
            companyID = miniDict['id']
            company = miniDict['name']
            try:
                bizBook.setdefault(companyID, company)
            except NameError:
                bizBook = {}
                bizBook.setdefault(companyID, company)
    return bizBook

def FetchMoreRecords():
    global indexNumber, pageNumber, bizBook
    #logging records retrieved during session
    pageNumberLog = []
    indexNumberLog = []
    while True:
        getCleanerData()
        pageNumberLog.append(pageNumber)
        indexNumberLog.append(indexNumber)
        sleep(random.random() + random.randint(2,4))
        before = len(bizBook)
        getCompanies()
        after = len(bizBook)
        if after > before:
            bizBookSave()
            print('records added was', (after - before))
        else:
            print('no new records')
            
indexNumber = 5
pageNumber=1
bizBookLoad()
FetchMoreRecords()

