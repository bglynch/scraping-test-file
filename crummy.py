html_doc = """<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title">
            <img src="smiley.gif" alt="image alt text">
            <b>The Dormouse's story</b>
        </p>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a> and
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
        """

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
print("=================1====================")
print(soup.title)
print(soup.title.text)
print(soup.title.name)
print("================2=====================")
print(soup.title.parent)
print(soup.title.parent.name)
print(soup.title.parent.text)
print("================3=====================")
print(soup.p)
print(soup.p['class'])
print("================4=====================")
print(soup.a)
def print_all():
    print(soup.find_all())
    '''
    [<html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a> and
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    </body></html>,
    
    <head><title>The Dormouse's story</title></head>, 
    
    <title>The Dormouse's story</title>,
    
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a> and
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    </body>,
    
    
    <p class="title"><b>The Dormouse's story</b></p>, 
    
    <b>The Dormouse's story</b>, 
    
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a> and
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    and they lived at the bottom of a well.</p>,
    
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>,
    
    <p class="story">...</p>]
    '''
print(soup.find_all('a'))
print(soup.find(id="link3"))
print("================5=====================")
for link in soup.find_all('a'):
    print(link.get('href'))
print("================6=====================")
print(soup.get_text())
print("================7=====================")

### Making the soup
with open("index.html") as fp:
    soup = BeautifulSoup(fp, "lxml")

# soup = BeautifulSoup("<html>data</html>")
print(soup)

print("================8=====================")

#### Kinds of Objects
soup = BeautifulSoup('<b id="boldest">Extremely bold</b>', "lxml")
print(soup)
print(type(soup))
# Tag
tag = soup.b
print(tag)
print(type(tag))
# Name
print(tag.name)
tag.name = "blockquote"
print(tag)
# Attributes
print(tag['id'])
print(tag.attrs)
print(tag.attrs['id'])
print('---add and modify attributes---')
tag['id'] = 'verybold'
tag["another-attribute"] = 1
tag["class"] = 'fish'
print(tag)
print('---delete attributes---')
del tag['id']
del tag['another-attribute']
print(tag)
# print(tag['id'])
# print(tag.get('id'))
print("================8=====================")
css_soup = BeautifulSoup('<p class="body"></p>', "lxml")
print(css_soup.p['class'])
css_soup = BeautifulSoup('<p class="body strikeout"></p>', "lxml")
print(css_soup.p['class'])

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', "lxml")
print(rel_soup.a)
print(rel_soup.a.text)
print(rel_soup.a.attrs)
print(rel_soup.a['rel'])
print('---add attributes---')
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
print(rel_soup.a.get_attribute_list('rel'))
print("================9=====================")
### NavigablelString
print(tag)
print(tag.string)
print(type(tag.string))
tag.string.replace_with("i am no longer bold")
print(tag)


print("================9=====================")
### Navigating the tree
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>and
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
# Navigating the tag names
print(type(soup))
print(soup.head)
print(soup.title)
print(soup.body.b)
print(soup.find_all('a'))

print("================10=====================")
# .contents and .children

head_tag = soup.head
print(head_tag)
print(head_tag.contents)
title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)
print(title_tag.contents[0][1:5])


print("================11=====================")
print(soup.contents)
print(len(soup.contents))
print(soup.contents[0].name)
print(title_tag.contents)
print(title_tag.contents[0])
text = title_tag.contents[0]
# print(text.contents)
print('---iterate over tags children---')
for child in title_tag.children:
    print(child)
print("================12=====================")
# .descendants

print(head_tag.contents)
for child in head_tag.descendants:
    print(child)
print(soup.body.contents)
print('---iterate over tags children---')
print(len(list(soup.children)))
print(len(list(soup.descendants)))
print("================13=====================")
# .string
print(title_tag)
print(title_tag.string)
print(head_tag)
print(head_tag.string)
print("================14=====================")
# strings and stripped_strings
for string in soup.strings:
    print(repr(string))
print('---stripped strings---')
for string in soup.stripped_strings:
    print(repr(string))

print("================15=====================")
###  GOING UP\
# parent
print('---parent---')

title_tag = soup.title
print(title_tag)
print(title_tag.parent)
print(title_tag.string.parent)
html_tag = soup.html
print(html_tag)
print(type(html_tag.parent))

# .parents
print('')
print('---parents---')

link = soup.a
print(link)
print(link.parent)
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

print("================16=====================")
print("===========GOING SIDEWAYS=====================")
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", "lxml")
print(sibling_soup.prettify())


print('')
print('---.next_sibling and .previous_sibling---')
print(sibling_soup.b.next_sibling)
print(sibling_soup.b.previous_sibling)
print(sibling_soup.c.previous_sibling)

link = soup.a
print(link)
print(repr(link.next_sibling))
print(link.next_sibling.next_sibling)

print('')
print('---.next_siblings and .previous_siblings---')

for sibling in soup.a.next_siblings:
    print(repr(sibling))

print("")
print("================17=====================")
print("======GOING BACK AND FORTH=============")

print('')
print('---.next_element and .previous_element---')
last_a_tag = soup.find("a", id='link3')
print(last_a_tag)
print(last_a_tag.next_sibling)
print(last_a_tag.next_element)
print(last_a_tag.previous_element)
print(last_a_tag.previous_element.next_element)

print('')
print('---.next_element and .previous_element---')
for element in last_a_tag.next_elements:
    print(repr(element))

print("")
print("================18=====================")
print("======SEARCHING THE TREE=============")

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>and
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print('')
print('---string---')
print(soup.find_all('b'))

print('')
print('------regular expression------')
import re
print('*** start with b ***')
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
    
print('*** contains letter t ***')
for tag in soup.find_all(re.compile("t")):
    print(tag.name)

print('')
print('---list---')
print(soup.find_all(["a", "b"]))

print('')
print('---True---')
for tag in soup.find_all(True):
    print(tag.name)

print('')
print('---Function---')
for tag in soup.find_all(True):
    print(tag.name)











