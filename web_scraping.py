from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


def get_parsed_url(url):
    # opens a response and gets the html of the page
    response = urlopen(url)
    html = response.read()
    response.close()
    # returns the parsed html as a soup
    return soup(html, "html.parser")


url = 'https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City'
page_soup = get_parsed_url(url)
table_rows = page_soup.table.find_all('tr')
# data I want to work with, don't need the first row or the last row
table_data = table_rows[1:-1]

populations = []
neighborhoods = []

for data in table_data:
    population = data.find_all('td')[2].get_text()
    neighborhood = data.find_all('td')[4].get_text()
    populations.append(population)
    neighborhoods.append(neighborhood)
    print("neighborhood: %s" % neighborhood,
          "\n", "population: %s" % population, "\n")
