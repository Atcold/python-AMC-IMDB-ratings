from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlencode

URL = 'https://www.imdb.com/search/title?'


def get_IMDB_rating(title):
    url = URL + urlencode({'title': title})
    conn = urlopen(url)
    soup = BeautifulSoup(conn, 'html.parser')
    movie = soup.find('div', 'lister-item mode-advanced')
    rating = movie.strong.text
    return rating


if __name__ == '__main__':
    title = input('Movie title (Glass): ')
    print(get_IMDB_rating(title))
