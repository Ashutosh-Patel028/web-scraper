import requests
from bs4 import BeautifulSoup
import pandas as pd

main_url = "https://free-proxy-list.net/#"

proxy = "http://129.154.225.163:8100"
# main_req = requests.get(main_url,proxies={'http':proxy,'https':proxy})
r = requests.get(main_url)

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



# def fetchAndSaveToFile():
#     r = requests.get(url)
#     with open(fileName, 'wb') as f:
#         f.write(r.content)
# fetchAndSaveToFile(main_url, "data/bags.html")


# import pandas as pd

# data = {'items': [], 'price': []}
# data['items'] = ['bag1', 'bag2', 'bag3']
# data['price'] = [100, 200, 300]
# df = pd.DataFrame.from_dict(data)
# df.to_csv('data/bags.csv', index=False)