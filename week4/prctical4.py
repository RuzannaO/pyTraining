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

df1 = pd.read_csv('netflix_titles.csv',parse_dates = ['date_added'])
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

movies = pd.read_csv('netflix_titles.csv', parse_dates=["date_added"] )
movies['cast'].fillna('None', inplace=True)
movies['duration_fixed']=movies['duration'].apply(cleanup)
movies1=movies[movies['cast'].str.contains('Antonio Banderas')]
movies1=movies1.sort_values(['duration_fixed','date_added'])

print(movies1[['cast','date_added','duration_fixed']])

# 6. Get number of movies added to Netflix in each year+month (2019 October - 15, 2017 September - 20 etc.). Sort by date and draw a plot of counts. Also draw a histogram of counts


def dtimes(x):
    dict_month={"01":"Jan","02":"Feb","03":"Mar","04":"Apr","05":"May","06":"Jun", "07":"Jul","08":"Aug","09":"Sep","10":"Oct","11":"Nov","12":"Dec"}

    return (str(x).split("-")[0]+" "+ dict_month[str(x).split("-")[1]])


def draw_plot(charttype, len,width, xaxis,yaxis,color:'lightgreen',linewidth:3,title,rotation,labelsize,name,xlabel,ylabel,skip):
    fig, name = plt.subplots(figsize=(len, width))
    if charttype=='bar':
        name.bar(xaxis, yaxis, color=color, linewidth=linewidth)
    elif charttype=='plot':
            name.plot(xaxis, yaxis, color=color, linewidth=linewidth)
    name.set(xlabel=xlabel, ylabel=ylabel, title=title)
    plt.xticks(xaxis, rotation=rotation)
    name.tick_params(labelsize=labelsize)
    name.set_xticks(name.get_xticks()[::skip])
    return plt.show()

movies = pd.read_csv('netflix_titles.csv')
movies['year_month'] = pd.to_datetime(movies['date_added']).dt.to_period('M')
movies1=(movies.groupby(['year_month']).count())
movies1.index=movies1.index.map(dtimes)
print(movies1.head())

draw_plot('plot',10,5,(movies1.index),movies1['show_id'],'lightgreen',3,'Number of movies by NETFLIX','vertical',8,"counts","date","number of movies",2)
draw_plot('bar',10,5,(movies1.index),movies1['show_id'],'purple',3,'Number of movies by NETFLIX','vertical',8,"counts","date","number of movies",2)


# 7.Sort dataset by date_added. Add a column, where each value will show how many days is past since the previous (row) addition to Netflix

movies = pd.read_csv('netflix_titles.csv')
movies['date'] = pd.to_datetime(movies['date_added']).dt.to_period('D')
movies.sort_values(by="date",inplace=True)
movies.reset_index(inplace=True)
list1=['0']
for i in range(1,len(movies['date'])):
    list1.append((str(movies['date'][i]-movies['date'][i-1]).split('*')[0][1:-1]))
for j in range(0,len(list1)):
    if list1[j]=='Day':
        list1[j]="1"
    elif list1[j]=='a':
        list1[j]='0'
list1=list(map(int,list1))
movies['days_passed']=list1
print(movies['days_passed'])
