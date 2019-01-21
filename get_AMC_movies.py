from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = 'https://www.amctheatres.com/movies'


def get_AMC_movies():
    conn = urlopen(URL)
    soup = BeautifulSoup(conn, 'html.parser')
    movies = soup.find_all(name='div', class_='MoviePostersGrid-poster')
    titles = tuple(m.find(name='a')['aria-label'] for m in movies)
    return titles


if __name__ == '__main__':
    print(' > Top-5 movies playing at AMC theatres')
    print(*get_AMC_movies()[:5], sep='\n')
