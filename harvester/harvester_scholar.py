from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from htlm_cleaner import cleanhtml
from urllib.parse import urlencode

from requests.api import get

import random
user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36']
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
# ]


def get_url(query):
    
    base_url = "https://scholar.google.com/scholar?hl=de&as_sdt=0%3I7&q="
    
    for element in query.split():
        base_url = base_url + element + "+"
    
    # return new base url with search keywords
    return get_proxy_url(base_url)

def get_proxy_url(url):
    
    payload = {
        'api_key': "13610693c488498ab7797051305c0b1c", 
        'url': url,
        'country_code': 'us'}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)

    return proxy_url

def get_content(query):
    
    url = get_url(query)
    headers = {'User-Agent': random.choice(user_agent_list)}

    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'lxml')

    articles = pd.DataFrame(columns = ['title', 'content', 'url'])

    # loop over articles
    #for item in soup.select("[data-lid]"): ## not working because of bot blocking
    for item in soup.find_all("div", {"class": "gs_r gs_or gs_scl"}):
        try:

            element = item.find("h3", attrs={"class": "gs_rt"})

            # get needed content
            title = element.a.text
            url = element.a["href"]
            content = item.find("div", {"class": "gs_rs"}).text

            # get citation count
            citation = item.find_all("div", {"class": "gs_fl"})
            for element in citation:
                
                if "Zitiert" in str(element):

                    citation = re.search(r"(?<=von: )\d+", str(element))[0]
            
            try:

                title = cleanhtml(title)
                content = cleanhtml(content)

            except:
                pass
            
            # save to dataframe
            articles.loc[int(citation)] = [title, content, url]
        
        except:

            pass

    articles = articles.sort_index(ascending=False)
    return articles