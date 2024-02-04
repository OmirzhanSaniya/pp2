from input import movies

def category_average(movies):
    total_score = 0
    category_name = input()
    category_movies = []
    for i in movies:
        if i["category"] == category_name:
            category_movies.append(i)
    for i in category_movies:
        total_score += i["imdb"] 
    average = total_score / len(category_movies)           
    return average

print(category_average(movies)) 