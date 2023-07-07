#Scraping data from https://free-proxy-list.net/# and save it to csv file
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://free-proxy-list.net/#"
r = requests.get(url)

with open("data/bags.html", "w") as f:
    f.write(str(r.content))

soup = BeautifulSoup(r.content, 'html.parser')
table_elmt = soup.find("table", class_="table table-striped table-bordered")
table_list = []
table_header = []
for th in table_elmt.find("thead").find_all("th"):
    table_header.append(th.get_text())
for val in table_header:
    print(val)
rows =[]
for tr in table_elmt.find("tbody").find_all("tr"):
    row=[]
    for td in tr.find_all("td"):
        row.append(td.get_text())
    rows.append(row)
print(table_header)
print(rows)
# table_list.append(table_header,rows)
# print(table_list)

def insertToCSV(table_header,rows):
    df=pd.DataFrame(rows,columns=table_header)
    df.to_csv("data/proxy.csv",mode='w',header=True,index=False)

insertToCSV(table_header,rows)