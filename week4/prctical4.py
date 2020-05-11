import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

2. Find number of movies released after 2015 with either Kevin Spacey or Leonardo DiCaprio starring.
df = pd.DataFrame(columns=['Name', 'Sirname', 'sex', 'appx age', 'status'])
df['Name']=['Arman','Narek','Norik','Zarmik']
df['status']=['student','tutor','student','tutor']
df.set_index('status',inplace=True)

print(df)

2. Find number of movies released after 2015 with either Kevin Spacey or Leonardo DiCaprio starring.

df1 = pd.read_csv('netflix_titles.csv',parse_dates = ['date_added'])
df1['cast'].fillna('None', inplace=True)
df2=df1[(df1['release_year']>2015) & ((df1["cast"].str.contains('Leonardo DiCaprio'))|(df1["cast"].str.contains('Kevin Spacey')))]
print(len(df2))



# 3.Find number of movies in Netflix for each director. Find a way to add this number to all rows with him. 
def direct(a):
    df4 = df1.groupby(['director']).count()
    df4.reset_index(inplace=True)
    df5 = df4[(df4["director"].str.contains(a))]
    list1 = list(df5['show_id'])
    return(sum(list1))

print(direct("Rene Bueno"))


# 4. Find a way to split cast to rows. So, for each movie that have, for example, 
# 10 actors in 'cast' column it will now have 10 rows with each actor in a row. 
# The other information should be the same for these 10 rows.

movies = pd.read_csv('netflix_titles.csv')
movies.set_index(['show_id','type', 'title', 'director', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'], inplace=True)
movies1=movies['cast'].str.split(',', expand=True).stack().reset_index()
movies1.columns=['show_id','type', 'title', 'director', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description','level_11','cast']
movies1.drop('level_11',axis=1,inplace=True)
print(movies1)


#5. Find all movies with Antonio Banderas starring. Sort by date and plot durations.


def cleanup(x):
    if 'Season' in x:
        return 30
    else:
        return int(x.split(" ")[0])


movies = pd.read_csv('netflix_titles.csv' )
movies['date_added'] = pd.to_datetime(movies['date_added'])
movies['cast'].fillna('None', inplace=True)
movies['duration_fixed']=movies['duration'].apply(cleanup)
# didn't use 'inplace' because it was returning a warning  - 'A value is trying to be set on a copy of a slice from a DataFrame"
movies1=movies[movies['cast'].str.contains('Antonio Banderas')]
# didn't use 'inplace' because it was returning a warning  - 'A value is trying to be set on a copy of a slice from a DataFrame"
movies1=movies1.sort_values(['duration_fixed','date_added'])
print(movies1[['title', 'date_added','duration_fixed']])
