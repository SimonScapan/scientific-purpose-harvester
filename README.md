# scientific-purpose-harvester

> Crawl Scientific Webpages for relevant papers. The easisets way to start your journey in the scientific jungle.
> - The SPH Team

*This Repro is build for only educational purposes!*

The Scientific-Purpose-Harvester (**SPH**) aims to build a dynamic possibility of crawling scientific webpages for relevant content, matching your questions.

![Landing-Page](/media/Landing-Page.png)

# Vision

Check Google Scholar for the best scientific results for your question, with the help of an easy-to-use Graphical User Interface.

# How to start

## Online

The easiest way to access the SPH.

Simply open [SPH](http://85.214.28.167:5001/), hosted by an SPH-Teammember.
This Website uses the svelte-Version of the SPH.

## Offline (Localy)

1. Clone the Repro
```console
git clone https://github.com/SimonScapan/scientific-purpose-harvester.git
```
2. Navigate into harvester
```console
cd harvester
```
3. Start the api.py to start the harvester
```console
python api.py
```
4. Open [Local Website](http://127.0.0.1:5000/) in your Browser
5. Shutdown Local Website with Using **CTRL+C** in your terminal

# How to use

1. Enter your question
![Question](/media/Question.png)
2. Hit the search button and wait for results.
3. Get a quick Overview of the best scientific papers for your questions. 
Follow a Link to get directly to the paper.
![Result](/media/Result.png)

# Used technology / Interesting Facts

* [Scraper-API](https://www.scraperapi.com/) allows us to crawl Google Scholar (or other Websites) without getting blacklisted.
  * A Free Plan of ScraperAPI is used. It allows 1000 free Requests per Month
  * If there is a Problem with the used API Key
    * Get your own free API-Key on the ScraperAPI Website
    * Replace the given API-Key with your personal API-Key in the [harvester_scholar.py](harvester/harvester_scholar.py) file
* [Svelte](https://svelte.dev/) allows us to use python file within the website
* The Papers are ranked by citation count

# Future Extensions

Here are some Idead for future extions. Feel free to fork this Project and add some of these, or your own Ideas!

- [ ] Free Text based NLP Training --> Q&A Pair generation --> Feed [Fancy Flash Cards](https://github.com/michael-spengler/ffc) with Content
- [ ] Build a Network of the cited articles. Who cited who? Where are conections?
- [ ] Build an Integration to some more Scientific Search Engines, like IEEE, arxiv, ...
- [ ] Generate with the Help of NLP abstracts for each Paper

# Thank you

Thank you for using the SPH.
If you have questions, feel free to reach out for the SPH-Team:

* **Jan Brebeck** - [Brebeck-Jan](https://github.com/Brebeck-Jan)
* **Andreas Bernrieder** - [Phantomias3782](https://github.com/Phantomias3782)
* **Simon Scapan** - [SimonScapan](https://github.com/SimonScapan)
* **Thorsten Hilbradt** - [Thorsten-H](https://github.com/Thorsten-H)
* **Niklas Wichter** - [NWichter](https://github.com/NWichter)
