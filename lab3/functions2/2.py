from input import movies

def above_5_5(movies):
    good_movies = []
    for i in movies:
        if i["imdb"] > 5.5:
            good_movies.append(i)
    return good_movies

print(above_5_5(movies))
