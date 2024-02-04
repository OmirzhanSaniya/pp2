from input import movies

def imdb(movies):
    for i in movies:
        if i["imdb"] > 5.5:
            return True   
    return False

print(imdb(movies))
