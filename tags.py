import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.amazon.in/s?k=bags&ref=nb_sb_noss_2")
with open("sample.html","w") as f:
    f.write(str(r.content))

with open("sample.html") as f:
    html_doc = f.read()

soup =BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
#print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.div)
# print(soup.div['class'])

# print(soup.find_all('div')[0])

# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))
#     print(link.get_text())

# s= soup.find(id="name")

# print(s.get_text())

# print(soup.select("div.italic"))  #use css selector
# print(soup.select("#name"))

# print(soup.find(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child)

# ulTag = soup.new_tag("ul")
# liTag = soup.new_tag("li")
# liTag.string = "Item-1"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "Item-2"
# ulTag.append(liTag)

# soup.body.insert(0,ulTag)
# with open("modified.html", "w") as f:
#     f.write(str(soup))

# cont = soup.find(class_="container")
# print(cont.has_attr("class"))

# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')

# print(soup.find_all(has_class_but_no_id))


# def has_content(tag):
#     return tag.has_attr('content')
# print(soup.find_all(has_content))