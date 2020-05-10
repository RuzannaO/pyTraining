import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame(columns=['Name', 'Sirname', 'sex', 'appx age', 'status'])
df['Name']=['Arman','Narek','Norik','Zarmik']
df['status']=['student','tutor','student','tutor']
df.set_index('status',inplace=True)

print(df)



df1 = pd.read_csv('netflix_titles.csv',parse_dates = ['date_added'])
df2=df1[(df1['release_year']>2015) & ((df1["cast"].str.contains('Leonardo DiCaprio'))|(df1["cast"].str.contains('Kevin Spacey')))]
print(len(df2))

def direct(a):
    df4 = df1.groupby(['director']).count()
    df4.reset_index(inplace=True)
    df5 = df4[(df4["director"].str.contains(a))]
    list1 = list(df5['show_id'])
    return(sum(list1))

print(direct("Rene Bueno"))
