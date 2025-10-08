favorite_movies = []


def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added.")


def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed.")
    else:
        print(f"Movie '{movie}' not found.")


def display_movies():
    print("Favorite Movies List:")
    for movie in favorite_movies:
        print(f"- {movie}")


def count_movies():
    if len(favorite_movies) > 0:
        movie_list_length = len(favorite_movies)
        print(f"There are {movie_list_length} movies in the list.")
    else:
        print("No movies found")


def find_movie(movie):
    if movie in favorite_movies:
        print(f"Movie '{movie}' found")
    else:
        print(f"Movie '{movie}' not found")


def clear_movies():
    favorite_movies.clear()
    print("Movies cleared")

display_movies()
add_movie("The Matrix")
add_movie("Bound")
count_movies()
remove_movie(favorite_movies[0])
display_movies()
