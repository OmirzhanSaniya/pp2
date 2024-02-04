from input import movies

def average(movies):
    total_score = 0
    for i in movies:
        total_score += i["imdb"]
    average = total_score / len(movies)
    return average    

print(average(movies))        