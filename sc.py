import bs4 as bs
# import requests
from urllib.request import urlopen  # for Python 3: from urllib.request import urlopen


# source = requests.get('http://www.daft.ie/11779060').text
# soup = BeautifulSoup(source, 'lxml')

URL = 'http://www.daft.ie/11779060'
sauce = urlopen(URL).read()
soup = bs.BeautifulSoup(sauce, 'lxml')
# print(soup.prettify())

    # <head>
    #     <title>Dartmouth Mews, Dartmouth Lane, Ranelagh, Dublin 6, South Dublin City - House For Sale</title>
    #         <meta name="description" content="Dartmouth Mews, Dartmouth Lane, Ranelagh, Dublin 6 - 2 bed end of terrace house for sale at &euro;660,000 from DNG Central. Click here for more property details." />
    #                     <meta property="twitter:title" content="Dartmouth Mews, Dartmouth Lane, Ranelagh, Dublin 6" />
    #                     <meta property="twitter:description" content="Dartmouth Mews, Dartmouth Lane, Ranelagh, Dublin 6 - 2 bed end of terrace house for sale at &euro;660,000 from DNG Central. Click here for more property details." />
    #                     <meta property="twitter:data1" content="&euro;660,000" />
    #                     <meta property="twitter:data2" content="2 Beds, 2 Baths" />

address = soup.find("meta", property="twitter:title")
price = soup.find("meta", property="twitter:data1")
beds_bath = soup.find("meta", property="twitter:data2")
x = soup.select(".ber-hover")

# print(address["content"] if address else "No meta title given")
# print(price["content"] if price else "No meta title given")
# print(beds_bath["content"] if beds_bath else "No meta title given")
    
# for img in soup.find_all('img', alt=True): 
#     img = soup.find('img', alt=True) 
#     print(img['alt'])
print(sauce)
print("=================")
print("=================")
print("=================")
print("=================")
print("=================")
# print(soup)
print("=================")
print("=================")
print("=================")
print("=================")
print(x.get('alt', ''))