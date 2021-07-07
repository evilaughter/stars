#https://en.wikipedia.org/wiki/List_of_brown_dwarfs
from bs4 import BeautifulSoup
import time,csv,requests
import pandas as pd
url= 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
browser=requests.get(url)
header=['name','distance','mass','radius']
soup=BeautifulSoup(browser.text,'html.parser')
table=soup.find_all('table')    
data=[]
rows=table[4].find_all('tr')
for tr in rows :
    td=tr.find_all('td')
    r=[i.text.rstrip() for i in td]
    data.append(r)

n=[]
d=[]
m=[]
r=[]

for i in range(1,len(data)):
    n.append(data[i][1])
    d.append(data[i][3])
    m.append(data[i][5])
    r.append(data[i][6])

df=pd.DataFrame(list(zip(n,d,m,r)),columns=header)    
df.to_csv('dwarfstars.csv')
