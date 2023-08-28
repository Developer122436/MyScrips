import requests
from bs4 import BeautifulSoup


def fetch_movie_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    movie_titles = [title.find("h3").text for title in soup.find_all(class_="article-title-description__text")]

    return movie_titles


def save_to_file(movie_titles, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            for title in reversed(movie_titles):
                file.write(title + '\n')
    except IOError as e:
        print(f"Error writing to file: {e}")


def main():
    URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
    FILE_NAME = 'movies.txt'

    movie_titles = fetch_movie_titles(URL)
    if movie_titles:
        save_to_file(movie_titles, FILE_NAME)
        print(f"Movie titles saved to {FILE_NAME}")


if __name__ == "__main__":
    main()
