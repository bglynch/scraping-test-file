from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pprint

def get_urls_for_location(url):
    pass



URL = 'http://www.daft.ie/dublin/houses-for-sale/ranelagh'
source = urlopen(URL).read()
soup = BeautifulSoup(source, 'lxml')


number_properties = soup.find(id="sr-sort").next_sibling.next_sibling.next_sibling.next_sibling.string
x = list(number_properties)
y=""
for char in x:
    if char.isdigit():
        y+=char
number_of_pages = (int(y)//20)*20
print(number_of_pages)


urls=[]
while number_of_pages>=0:
    URL = 'http://www.daft.ie/dublin/houses-for-sale/ranelagh/?offset='+str(number_of_pages)
    source = urlopen(URL).read()
    soup = BeautifulSoup(source, 'lxml')
    divs = soup.find_all('div', class_="search_result_title_box")
    
    for div in divs:
        a=div.find('a')
        urls.append("http://www.daft.ie" + a['href'])
    
    print(urls)
    number_of_pages -= 20
        
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(urls)
print(len(urls))
