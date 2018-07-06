from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json
import pprint
import getlinks

URL = 'http://www.daft.ie/dublin/houses-for-sale/ranelagh/57-clonskeagh-road-ranelagh-dublin-1765414'
source = urlopen(URL).read()
soup = BeautifulSoup(source, 'lxml')

# Ber Number
ber_number = soup.find("div", attrs={"id": "smi-ber-details"}).next_sibling
number_from_text = [int(s) for s in ber_number.split() if s.isdigit()]


# Data from javascript <script>
parsed_list = []
# get data kwith regex
json_string = re.findall(r"{\W\w.*\W}", soup.text)[1].split(',"')

# remove unwanted characters and append to empty list
for i in json_string:
    parsed_list.append(i.replace('"', '').replace('{', '').replace('}', ''))

pp = pprint.PrettyPrinter(indent=4)

# split list into 2 lists
data_key = [i.split(':', 1)[0] for i in parsed_list]
data_value = [i.split(':', 1)[1] for i in parsed_list]

# combine 2 lists into dictionary
dictionary = dict(zip(data_key, data_value))

# update dictionarry
property_area = dictionary.get('property_title').split(', ')[-1]

dictionary.update({'ber_number': (number_from_text)[0], 'property_area': property_area})

pp.pprint(dictionary)


pp.pprint(getlinks.urls)


