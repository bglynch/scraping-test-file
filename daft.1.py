from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json


URL = 'http://www.daft.ie/dublin/houses-for-sale/ranelagh/57-clonskeagh-road-ranelagh-dublin-1765414'
source = urlopen(URL).read()
soup = BeautifulSoup(source, 'lxml')




# Address
address = soup.find(property="twitter:title").get('content')
print(address)

# County

# Sub Area
sub_area = address.split(', ')
print(sub_area[-1])

# Price
print('')
price = soup.find(property="twitter:data1").get('content')
number_from_text = int(('').join([s for s in price.split()[0] if s.isdigit()]))
print(number_from_text)

# Ber Rating
print('')
ber_rating = soup.find("div", attrs={"id": "smi-ber-details"}).img.attrs['alt']
print(ber_rating)

# Ber Number
print('')
ber_number = soup.find("div", attrs={"id": "smi-ber-details"}).next_sibling
number_from_text = [int(s) for s in ber_number.split() if s.isdigit()]
print((number_from_text)[0])

# Letting Agent
print('')
agent = soup.find("div", attrs={"class": "agent-info-list"}).a.text
print(agent)

# Floor Area
floor_area = soup.find('strong', text = re.compile('loor')).next_sibling
print(floor_area)

# Facilities
facilities = soup.find('h3', text = re.compile('Facilities')).next_sibling.text
facilities2 = soup.find(id="facilities").get_text()
print(facilities)
print(facilities2)

data = soup.find_all('script')
print(len(data))
print(data[0].text)


for s in soup.find_all('script'):
    if 'var trackingParam' in s.text:
        print(type(s))
        print(s)
        print(s.text)
        print('=============================next element=====================')
        print(s.next_element)
        print(type(s.next_element))
        x = s.next_element.split("{")[3]
        print(x)
        # print re.findall(r"\w", s.next_element)
        print(re.findall(r"{\W\w.*\W}", s.text))
        print(type(re.findall(r"{\W\w.*\W}", s.text)))