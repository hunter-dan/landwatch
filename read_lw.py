import csv
import requests
from BeautifulSoup import BeautifulSoup

# Define states to scrape
states = ["30", "31", "56", "41"]  # California, Colorado, Montana, Idaho
properties = []

# Scrape from all states
for state in states:

    # Scrape multiple pages
    page = 1
    while page <= 30:
        url = 'https://www.landwatch.com/default.aspx?ct=R&type=5,{};13,12;268,6843&pg={}'.format(state, page)
        page = page + 1
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html)
        dataset = soup.find('div', attrs={'class': 'left resultscontainer'})

        # Scrape titles of properties and append into list
        props = []
        for propName in dataset.findAll('div', attrs={'class': 'propName'}):
            name = str(propName.find('a').text.replace('&nbsp;', ''))  # type: str
            name = name.replace('  ', ', ')
            name = name.replace('$', ', $')
            name = name.replace(' Acres', '')
            props.append(name)

        # Split list into matrix
        for name in props:
            splitName = name.split(', ')
            properties.append(splitName)

# write to csv
with open('./land.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Size (Acres)", "City", "County", "State", "Price", "Notes"])
    writer.writerows(properties)
