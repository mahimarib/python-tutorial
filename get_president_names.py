from web_scraping import get_parsed_url

url = 'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States'
page_soup = get_parsed_url(url)
tables = page_soup.findAll('table', {'class': 'wikitable'})
table_rows = tables[0].find_all('tr')
# the first row does not include the names of presidents
# created a new array with with the actual working data
working_data = table_rows[2:]

presidents = []

for row in working_data:
    # because some rows do not contain the presidents name,
    # had to differentiate the rows
    if len(row.find_all('td')) >= 4:
        president = row.find_all('td')[3].a.getText()
        presidents.append(president)
        # print(president)

print(presidents)
