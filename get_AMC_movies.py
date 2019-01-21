from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_AMC_movies():
    # AMC URL
    URL = 'https://www.amctheatres.com/movies'

    # Open the AMC page
    conn = urlopen(URL)
    # reply = conn.read()
    # print(reply)

    # Get the movies
    soup = BeautifulSoup(conn, 'html.parser')
    movies = soup.find_all(name='div', class_='MoviePostersGrid-poster')
    titles = tuple(m.find(name='a')['aria-label'] for m in movies)
    return titles


if __name__ == '__main__':
    print(' > Movies playing at AMC theatres')
    print(*get_AMC_movies()[:5], sep='\n')
