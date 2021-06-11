import random
from googlesearch import search
import requests
from requests.api import get
from bs4 import BeautifulSoup 
import pandas as pd

def search_engine_result(query):
    '''
    input: query = give your question to the tool

    process:
        * search google for the given query
        * remove blacklistet webpages
        * choose random five results

    return: five random google results without blacklistet webpages
    '''

    # add some websites which you don't want to see in your analysis
    blacklist = ['wikipedia', 'youtube']

    # result list of links to webpages
    links = []

    # get google search engine results with given parameters
    for link in search(query, tld="co.in", lang='de', num=20, stop=20, pause=2): 

        # cick the blacklistet webpages
        if not [string for string in blacklist if(string in link)]:
            links.append(link) 

    # pick random five webpages for further crawling
    return random.sample(links, 5)

def get_page_content(url):
    '''
    input: url = give the required url

    process:
        * webpage is parsed by BeautifulSoup
        * get Title of Webpage
        * get amount of <p> Tags in page
        * search for largest <p> tag

    return: webpage title and largest <p> Tag content
    '''

    # Request webpage from WWW with request package
    page = requests.get(url)

    # getting the different html content parsed by BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')

    # get title of Webpage
    title = soup.title.text

    # get amount of <p> elements in html file
    tags = soup.findAll('p')

    # add all <p> elements into list
    contents = []
    for i in range(len(tags)):
        contents.append(soup.select('p')[i].text.strip()) # delete all leading and tailing whitespaces from string with .strip()

    # save only the longest <p> element
    try:
        content = max(contents, key = len)
    except:
        content = "sorry, no results"
    
    # return title and content of given webpage 
    return title, content

def get_work_done(question):
    '''
    input: question = something you want to know from the web

    process:
        * search google for your question
        * get 5 webpages
        * get their title and content

    return: dataframe with = |title|content|url|
    '''

    articles = pd.DataFrame(columns = ['title', 'content', 'url'])
    urls = search_engine_result(question)
    for url in urls:
        title, content = get_page_content(url)
        articles.loc[len(articles)] = [title, content, url]

    return articles