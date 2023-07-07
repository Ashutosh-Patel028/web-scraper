#Tried to scrap the data from amazon.com but it was not possible because of the dynamic nature of the website.
from bs4 import BeautifulSoup

with open("data/bags.html") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

with open("test2.html","r") as f:
    test2=f.read()

soup2 = BeautifulSoup(test2, 'html.parser')
# print(soup2.prettify())

item_div = soup.find_all("div", class_="a-section a-spacing-none puis-padding-right-small s-title-instructions-style")

print(item_div[0])
print(item_div[0].get_text())
print((item_div[0]).find("a").get("href"))


# with open("test.html","+a") as f:
#     for item in item_div:
#         f.write(str(item))

# soup2.body.insert(0,str(item_div[0]))
# with open("test2.html","w+") as f:
#     f.write(str(soup2))
# print(soup2.prettify())