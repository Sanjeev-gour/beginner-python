import csv

#using normal python code 
'''
def cal_ratings_stats(data,industry=None):
    ratings = []
    for row in data:
        if row[3]!='NULL' and (not industry or row[1]==industry):
            ratings.append(float(row[3]))
    max_rating = max(ratings)
    min_rating = min(ratings)
    avg_rating = sum(ratings)/len(ratings)
    return max_rating, min_rating, avg_rating
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                            
with open("movies.csv") as f:
    data= list(csv.reader(f))
    header = data[0]
    data = data[1:]


max_rating, min_rating, avg_rating = cal_ratings_stats(data)
print(f"All records: Min rating={min_rating}, Max rating = {max_rating}, Average rating={avg_rating}")

max_rating, min_rating, avg_rating = cal_ratings_stats(data,industry="Bollywood")
print(f"All records: Min rating={min_rating}, Max rating = {max_rating}, Average rating={avg_rating}")

max_rating, min_rating, avg_rating = cal_ratings_stats(data,industry="Hollywood")
print(f"All records: Min rating={min_rating}, Max rating = {max_rating}, Average rating={avg_rating}")
'''

#using pandas library

import pandas as pd

df = pd.read_csv("movies.csv")

#print(df)
'''
print(df.head())#will print only few rows from top

print(df.tail(7))#will print only few rows from bottom

print(df.sample())#will print randomly

print(df[2:6])#will print from specific index to specific index

print(df.shape)#number of rows and columns
'''

#can be printed in both ways
#print(df["imdb_rating"])#class object
#print(df.imdb_rating)#property

#print("Minimum rating:",df.imdb_rating.min(),"Maximum rating:",df.imdb_rating.max(),"Average rating:",df.imdb_rating.mean())


# if to print ratings for specific industry 

df_b = df[df.industry=="Bollywood"]
df_h = df[df.industry=="Hollywood"]

print(df_b)
print("Minimum rating of bollywood:",df_b.imdb_rating.min(),"Maximum rating of bollywood:",df_b.imdb_rating.max(),"Average rating of bollywood:",df_b.imdb_rating.mean())


print(df_h)
print("Minimum rating of Hollywood:",df_h.imdb_rating.min(),"Maximum rating of Hollywood:",df_h.imdb_rating.max(),"Average rating of Hollywood:",df_h.imdb_rating.mean())




