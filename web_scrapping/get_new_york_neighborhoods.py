from web_scraping import get_parsed_url

url = 'https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City'
page_soup = get_parsed_url(url)
table_rows = page_soup.table.find_all('tr')
# data I want to work with, don't need the first row or the last row
table_data = table_rows[1:-1]

for data in table_data:
    population = data.find_all('td')[2].get_text()
    neighborhood = data.find_all('td')[4].get_text()
    print("neighborhood: %s" % neighborhood, "\n",
          "population: %s" % population, "\n")
