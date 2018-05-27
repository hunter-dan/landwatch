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
    while page <= 1:

        # Progress tracking
        stateName = ''
        if state == '30':
            stateName = "California"
        elif state == '31':
            stateName = "Colorado"
        elif state == '56':
            stateName = "Montana"
        elif state == '41':
            stateName = "Idaho"
        print "Scraping " + str(stateName) + " Page" + " " + str(page)

        url = 'https://www.landwatch.com/default.aspx?ct=R&type=5,{};13,12;268,6843&pg={}'.format(state, page)
        page = page + 1
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html)
        dataset = soup.find('div', attrs={'class': 'left resultscontainer'})

    # Scrape titles and URLs of properties and append into list
        props = []

        for propName in dataset.findAll('div', attrs={'class': 'propName'}):
            name = str(propName.find('a').text.replace('&nbsp;', ''))  # type: str
            name = name.replace(' ,', "-,")
            name = name.replace('  ', ', ')
            name = name.replace('$', ', $')
            name = name.replace(' Acres', '')
            commaCount = 5 - name.count(', ')
            if commaCount > 0:
                name = name + (', '*commaCount)
            href = propName.find('a')['href']
            propId = href[-9:].replace('/','')
            propId = propId.replace('d','')
            name = name + ", " + href + ", " + propId

            # follow listing links
            listUrl = 'https://www.landwatch.com/'+ href
            listResp = requests.get(listUrl)
            listHtml = listResp.content
            listSoup = BeautifulSoup(listHtml)
            listFeatures = listSoup.find('div', attrs = {'class': 'left dtlefthalf margintop'})

            features = []

             # pull listing details
            ftag1 = 'clear bold accent margintop'
            ftag2 = 'clear pattname bold'
            ftag3 = 'clear pattname'
            ftag4 = 'pattvalue'

            for propFeatures in listFeatures.findAll('div', attrs={'class': [ftag1, ftag2, ftag3, ftag4]}):
                featText = str(propFeatures.getText().replace('&nbsp;', ''))
                featText = featText.replace('Agent/Broker Information', '')
                featText = featText.replace('Website URL:', '')
                featText = featText.replace('Click here', '')
                if featText:
                    features.append(featText)

            row = str(name) + ', ' + str(features)
            props.append(row)

        # Split list into matrix
        for row in props:
            splitRow = row.split(', ')
            properties.append(splitRow)



# write to csv
with open('./land.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Size (Acres)", "City", "County", "State", "Price", "Notes", "Link", "Property ID"])
    writer.writerows(properties)

print "We Done."