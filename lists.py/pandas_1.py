import csv

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



