import requests
from bs4 import BeautifulSoup

def fetch_genre_from_movie_page(movie_url, mood):
    HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    response = requests.get(movie_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    genres=[]
    for td in soup.find_all('a', class_='ipc-chip ipc-chip--on-baseAlt'):
        genres.append(td.span.text)
    if any(genre.lower() in mood for genre in genres):
        description = soup.find('span', class_='sc-466bb6c-0 kJJttH').text
        return genres, description


def fetch_movies_from_imdb(mood ): 
    HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    print(mood)
    url = 'https://www.imdb.com/chart/top'
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')
    movies = []
    count = 0
    for td in soup.find_all('li' , class_='ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent'):
        title = td.find('h3' , class_='ipc-title__text').text.split(".")[1]
        year = td.find('span' , class_='sc-14dd939d-6 kHVqMR cli-title-metadata-item').text
        movie_url = 'https://www.imdb.com' + td.find('a' , class_='ipc-title-link-wrapper')['href']
        genres_desc = fetch_genre_from_movie_page(movie_url , mood)
        if genres_desc:
            movies.append((title, year, genres_desc[1] ))
            count += 1
        if count == 5:
            break
    return movies

