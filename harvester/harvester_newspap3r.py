from newspaper import Article       # pip3 install newspaper3k
from googlesearch import search


def search_engine_result(query):
    '''
    input: query = give your question to the tool

    process:
        * search google for the given query
        * remove blacklistet webpages
        * choose random five results

    return: five random google results without blacklistet webpages
    '''

    # result list of links to webpages
    links = []

    # get google search engine results with given parameters
    for link in search(query, tld="co.in", lang='de', num=20, stop=20, pause=2): 

        links.append(link) 

    return links


def get_article(url):
    '''
    describe this shit
    '''

    try: 
        article = Article(url)
        article.download()
        article.parse()

        title = article.title
        authors = article.authors
        publish_date = article.publish_date
        text = article.text

        article.nlp()
        
        keywords = article.keywords
        summary = article.summary

        return title, authors, publish_date, text, keywords, summary

    except: return "error"
    
def get_it_done(question):
    '''
    input: question = something you want to know from the web

    process:
        * search google for your question
        * get 5 webpages
        * get their title and content

    return: dataframe with = |title|content|url|
    '''

    articles = pd.DataFrame(columns = ['title', 'authors', 'publish_date', 'text', 'keywords', 'summary', 'url'])
    urls = search_engine_result(question)
    for url in urls:
        title, authors, publish_date, text, keywords, summary = get_article(url)
        articles.loc[len(articles)] = [title, authors, publish_date, text, keywords, summary, url]

    return articles