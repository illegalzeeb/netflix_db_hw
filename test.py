
import sqlite3
from copy import deepcopy


def search_by_title(movie_title : str) -> dict:
    movie_data = {}
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT title, country, release_year, listed_in, description FROM 'netflix' WHERE title = ? ORDER BY release_year DESC LIMIT 1", (movie_title,))
        for row in cursor.fetchall():

            movie_data["title"] = row[0]
            movie_data["country"] = row[1]
            movie_data["release_year"] = row[2]
            movie_data["genre"] = row[3]
            movie_data["description"] = row[4]

    return movie_data


def search_by_date(start_date, end_date : str) -> list[dict]:
    """
    #Поиск в базе данных по диапазону лет выпуска, возвращает 100 записей
    """
    movie_data = {}
    response = []
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT title, release_year FROM 'netflix' WHERE release_year BETWEEN ? AND ? ORDER BY release_year DESC LIMIT 100", (start_date, end_date))
        for row in cursor.fetchall():

            movie_data["title"] = row[0]
            movie_data["release_year"] = row[1]

            response.append(deepcopy(movie_data))

        return response


def search_by_children_rating() -> list[dict]:
    """
    #Поиск в базе данных по детскому рейтингу, возвращает 100 записей
    """
    movie_data = {}
    response = []
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT title, rating, description FROM 'netflix' WHERE rating = 'G' LIMIT 100")
        for row in cursor.fetchall():

            movie_data["title"] = row[0]
            movie_data["rating"] = row[1]
            movie_data["description"] = row[2]

            response.append(deepcopy(movie_data))
        return response


def search_by_family_rating() -> list[dict]:
    """
    #Поиск в базе данных по семейному рейтингу, возвращает 100 записей
    """
    movie_data = {}
    response = []
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT title, rating, description FROM 'netflix' WHERE rating = 'G' OR rating = 'PG' OR rating = 'PG-13' LIMIT 100")
        for row in cursor.fetchall():

            movie_data["title"] = row[0]
            movie_data["rating"] = row[1]
            movie_data["description"] = row[2]

            response.append(deepcopy(movie_data))
        return response


def search_by_genre(genre: str) -> list[dict]:
    """
    Поиск в базе данных по жанру, возвращает 10 записей самых свежих записей
    """
    movie_data = {}
    response = []
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT title, description FROM 'netflix' WHERE listed_in LIKE ? ORDER BY date_added DESC LIMIT 10", ('%'+genre+'%',))
        for row in cursor.fetchall():

            movie_data["title"] = row[0]
            movie_data["description"] = row[1]

            response.append(deepcopy(movie_data))
        return response


def search_by_actors(actor_a, actor_b: str) -> set:
    """
    Ищет актеров, игравших с парой указанных актеров
    """
    movie_data = []
    response = []
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT 'cast' FROM 'netflix' WHERE 'cast' LIKE ? AND 'cast' LIKE ?", ('%'+actor_a+'%', '%'+actor_b+'%',))
        for row in cursor.fetchall():
            print(row)
            movie_data = row.split(", ")

            response.append(deepcopy(movie_data))
        return set(response)


def search_by_type(type, year, genre) -> set:
    """
    Ищет фильм по параметрам
    """
    movie_data = {}
    response = []
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT title, description FROM 'netflix' WHERE type LIKE ? AND listed_in LIKE ? AND release_year = ?", ('%'+type+'%', '%'+genre+'%', year))
        for row in cursor.fetchall():
            movie_data["title"] = row[0]
            movie_data["description"] = row[1]

            response.append(deepcopy(movie_data))
        return response


test_data = search_by_type("Movie", "2017", "Drama")
print(test_data)
print(type(test_data))


#AND 'cast' LIKE ?  '%'+actor_b+'%'