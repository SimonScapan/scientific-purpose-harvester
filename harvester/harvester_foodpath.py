import random
import googlesearch
import requests
from requests.api import get
from bs4 import BeautifulSoup 
import pandas as pd
import ssl
from html_cleaner import cleanhtml



ssl._create_default_https_context = ssl._create_unverified_context

def search_engine_result(query):
    '''
    input: query = give your question to the tool

    process:
        * search google for the given query
        * remove blacklistet webpages

    return: google results without blacklistet webpages
    '''

    # add some websites which you don't want to see in your analysis
    blacklist = ['wikipedia', 'youtube']

    # result list of links to webpages
    links = []
    results=googlesearch.search(query, lang='de')
    results=[x for x in results if "http" in x]
    # get google search engine results with given parameters
    for link in results: 
        # cick the blacklistet webpages
        if not [string for string in blacklist if(string in link)]:
            links.append(link) 

    # pick random five webpages for further crawling
    return links

def get_page_content(url):
    '''
    input: url = give the required url

    process:
        * webpage is parsed by BeautifulSoup
        * get Title of Webpage
        * get amount of <p> Tags in page
        * append all <p> tags

    return: webpage title and all <p> Tag content
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
    content = ''
    for i in range(len(tags)):
        content = content + '' + str(soup.select('p')[i].text.strip()) # delete all leading and tailing whitespaces from string with .strip()

    # return title and content of given webpage 
    return cleanhtml(title), cleanhtml(content)


def get_work_done(question):
    '''
    input: question = something you want to know from the web

    process:
        * search google for your question
        * get their title and content
        * sort content by length

    return: dataframe with = |title|content|url|
    '''

    articles = pd.DataFrame(columns = ['Title', 'Content', 'URL', 'content_length'])
    urls = search_engine_result(question)
    for url in urls:
        title, content = get_page_content(url)  # get title and content of webpage
        content_length = len(content)           # sort by content length
        content = content[:1000] + ' ...'       # truncate content to 500 digits
        articles.loc[len(articles)] = [title, content, url.rstrip('/'), content_length]
    
    articles.sort_values(by=['content_length'], ascending=False, inplace=True)  # sort length ascending
    articles.drop(['content_length'], axis=1, inplace=True)                     # delete help column content_length
    
    articles['URL'] = '<a href=' + articles['URL'] + '><span>' + articles['URL'] + '</span></a>'

    return articles