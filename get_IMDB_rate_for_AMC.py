from get_AMC_movies import get_AMC_movies
from get_IMDB_rating import get_IMDB_rating

if __name__ == '__main__':
    movies = get_AMC_movies()
    ratings = tuple(get_IMDB_rating(movie) for movie in movies[:10])
    print('> IMDB ratings of 10-top movies at AMC\n')
    print(*zip(movies, ratings), sep='\n')
