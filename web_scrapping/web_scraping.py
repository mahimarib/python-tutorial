from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


def get_parsed_url(url):
    # opens a response and gets the html of the page
    response = urlopen(url)
    html = response.read()
    response.close()
    # returns the parsed html as a soup
    return soup(html, "html.parser")
