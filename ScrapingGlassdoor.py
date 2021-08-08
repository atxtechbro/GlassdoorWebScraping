from bs4 import BeautifulSoup
import json
from random import randint
import re
import requests
from time import sleep

locID = 0
def turnThePage(locID):
    headers={'User-Agent': 'Mozilla/5.0'}
    bizBook = {}
    while True:
        url = "https://www.glassdoor.com/Explore/browse-companies.htm?overall_rating_low=0&page=1&isHiringSurge=0&locId={}&locType=N&locName=US".format(locID)
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        a = str(soup.find('article').find('script').next.replace('\n', '').strip())
        regex = r"JSON MESSAGE BUNDLE - do not remove\"}},(.*)"
        regex_response = re.search(regex, a).group(1)
                
        d = json.loads('{' + regex_response[:-1])['apolloState']
        json_data = json.dumps(d)
        j = json.loads((json_data.replace(r"\\", '')))
                
        try:
            for k in j['ROOT_QUERY'].keys():
                if k.startswith('employerJobsInfo'):
                    start = k.find('id')
                    end = k.find('name')
                    id_ = k[start+4:end-2]
                    biz = k[end+7:-4]
                    print(biz)
                    bizBook[id_] = biz
        except KeyError as e:
            pass
        locID += 10
        print(len(bizBook))
        print(bizBook)
        sleep(randint(8,13))
        
turnThePage(locID)
