import csv 
data1 =[]
data2 =[]
with open('brightstars.csv') as f :
    cr = csv.reader(f)
    for row in cr :
        data1.append(row)
header1= data1[0]        
starsdata1=data1[1: ]

with open('dwarfstars.csv') as f :
    cr = csv.reader(f)
    for row in cr :
        data2.append(row)
header2= data2[0]        
starsdata2=data2[1: ]

headers=header1+header2
mergestars=[]
for i,row in enumerate(starsdata1):
    mergestars.append(starsdata1[i]+starsdata2[i])


with open('mergedstars.csv',"a+") as f :
    cw=csv.writer(f)
    cw.writerow(headers)
    cw.writerows(mergestars)
    

