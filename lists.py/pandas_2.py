import pandas as pd

df = pd.read_csv("movies.csv")

'''
#print(df.industry)

print(df.industry.unique())

print(df.language.unique())

print(df.industry.value_counts())

print(df.language.value_counts())


#if only interested in specific columns 

df_new =df[["title","imdb_rating","industry"]]

print(df_new)

#if only interested in specific rows

df_new1 = df[(df.release_year>2000) & (df.release_year<2010)]

print(df_new1)

print(df.studio.unique())

print(df[df.studio == 'Marvel Studios'])


'''
'''
print(df.describe())


print(df.info())

#to print which movie has maximum imdb rating 

print(df[df.imdb_rating == df.imdb_rating.max()])
'''

#if need to derive a column from existing column 

df["Age"] = (df.release_year).apply(lambda x:2024-x)

print(df)

df["profit"] = df.apply(lambda x: x['revenue']-x['budget'], axis=1)
print(df.head(4))


#here the numbers are index we can set movies as index intead of numbers

df.set_index("title",inplace =True)

print(df.head(4))

print(df.index)

print(df.loc['Titanic']) # will print the inforamtion about index Titanic

#if we want to print using number then 

print(df.iloc[4])


#if want to replace the index '

df.reset_index(inplace=True)
print(df.head(4))