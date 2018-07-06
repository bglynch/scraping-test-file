from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


match = soup.title.text                         #finds the title text
match2 = soup.div                               # finds the content from the FIRST div
match3 = soup.find('div', class_='footer')       # finds div with the class='footer'

article = soup.find('div', class_='article')       # 
print(article)
print('======================')
headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)
print('======================')

for article in soup.find_all('div', class_ = 'article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    
    print()
