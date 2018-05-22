import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://www.landwatch.com/Colorado_land_for_sale/Land'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
dataset = soup.find('div', attrs={'class': 'left resultscontainer'})

props = []
for propName in dataset.findAll('div', attrs={'class': 'propName'}):
	name = propName.find('a').text.replace('&nbsp;', '')
	props.append(name)
print(props)

# with open('./land.csv', 'wb') as outfile:
#     writer = csv.writer(outfile, delimiter=' ')
#     writer.writerow(["Name"])
#     writer.writerows(props)
