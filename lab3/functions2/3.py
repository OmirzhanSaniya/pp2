from input import movies

def category(movies):
    category_name = input()
    category_movies = []
    for i in movies:
        if i["category"] == category_name :
            category_movies.append(i)
    return category_movies

print(category(movies))