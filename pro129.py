import pandas as pd 
df=pd.read_csv('dwarfstars.csv')
df=df.dropna()
df["radius"]=df["radius"].astype('float')*0.102763
df['mass']=df['mass'].apply(lambda x:x.replace('$','').replace(',','')).astype('float')
df['mass']=df['mass']*0.000954588763
df.to_csv('convertedstars.csv')

