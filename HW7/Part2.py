# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:06:07 2020

@author: annorm
"""

"""FIND THE BEST AND WORST RATED MOVIES IN A GENRE BETWEEN A PERIOD OF TIME"""

import json

if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())

min_year = int(input("Min year => "))
print(min_year)
max_year = int(input("Max year => "))
print(max_year)
w1 = input("Weight for IMDB => ")
print(w1)
w1 = float(w1)
w2 = input("Weight for Twitter => ")
print(w2+'\n')
w2 = float(w2)

cinema = []
comb_rating= dict()

"""TAKE ALL THE MOVIES BETWEEN THE MIN AND MAX YEARS AND PUTS THEM INTO A LITTLE """
for films in movies:
    if int(movies[films]["movie_year"]) >= min_year and int(movies[films]["movie_year"]) <= max_year:
        cinema.append(films)

"""FIND THE COMBINED RATING FOR THE MOVIES"""
for movie in cinema:
    if movie not in ratings or len(ratings[movie]) < 3:
        continue
    else:
        comb_rating[movie] = (w1 * (movies[movie]["rating"]) + w2 * (sum(ratings[movie])/len(ratings[movie]))) / (w1 + w2)

end = False
while not end:
    genre = input("What genre do you want to see? ")
    print(genre)
    if genre.lower() != "stop":
        genre_movies = []

        for keys in list(comb_rating.keys()):
            if genre.title() in movies[keys]["genre"]:
                genre_movies.append((comb_rating[keys], keys))

        genre_movies = sorted(genre_movies, reverse=True)
        if len(genre_movies) == 0:
            print('')
            print("No", genre.title(), "movie found in", min_year, "through", max_year, end = "\n\n" )
        else:
            print('')
            print("Best:")
            print(" "*7, "Released in", str(movies[genre_movies[0][1]]["movie_year"]) + ",",  movies[genre_movies[0][1]]["name"], "has a rating of {:.2f}".format(genre_movies[0][0]), end = "\n\n" )
            print("Worst:")
            print(" "*7, "Released in", str(movies[genre_movies[-1][1]]["movie_year"]) + ",",  movies[genre_movies[-1][1]]["name"], "has a rating of {:.2f}".format(genre_movies[-1][0]), end = "\n\n" )

    elif genre.lower() == "stop":
        end = True
