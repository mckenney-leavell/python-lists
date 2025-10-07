movie_collection = [
    ("Matrix", "Watchowskis", 1985),
    ("Shawshank", "Darabont", 1994),
    ("The Godfather", "Coppola", 1972),
    ("Bound", "Watchowskis", 1980)
]

def add_movie(title, director, year):
    new_movie = (title, director, year)
    movie_collection.append(new_movie)
    print(f"Movie '{title}' directed by {director} added to the collection.")

def display_movies():
    print("Movie Collection:")
    for title, director, year in movie_collection:
        print(f"Title: {title}, Director: {director}, Year: {year}")
    
def search_by_director(director):
    movies_by_director = []
    for movie in movie_collection:
        title, movie_director, year = movie 
        if movie_director.lower() == director.lower():
            movies_by_director.append(movie)
    return movies_by_director

display_movies()

add_movie("Dark Knight", "Nolan", 2008)

display_movies()

books_by_watchowskis = search_by_director("Watchowskis")
print("Movies by the Watchowskis:")
for title, director, year in books_by_watchowskis:
    print(f"Title: {title}, Year: {year}")