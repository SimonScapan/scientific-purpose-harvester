from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}


def get_url(query):
    
    base_url = "https://scholar.google.com/scholar?hl=de&as_sdt=0%2C5&q="
    
    for element in query.split():
        base_url = base_url + element + "+"
    
    # return new base url with search keywords
    return base_url


def get_content(query):
    
    url = get_url("machine learning")

    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'lxml')

    articles = pd.DataFrame(columns = ['title', 'content', 'url'])

    # loop over articles
    for item in soup.select("[data-lid]"):

        try:
            
            # get needed content
            title = item.select("h3")[0].get_text()
            url = item.select('a')[0]['href']
            content = item.select('.gs_rs')[0].get_text()

            # get citation count
            citation = item.select("a")
            for element in citation:
                
                if "Zitiert" in str(element):

                    citation = re.search(r"(?<=von: )\d+", str(element))[0]
            
            # save to dataframe
            articles.loc[int(citation)] = [title, content, url]
        
        except:

            pass
        
    articles = articles.sort_index(ascending=False)
    return articles