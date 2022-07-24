import sqlite3

def search_by_title(movie_title : str) -> list[dict]:
    """
    Поиск в базе данных по названию фильма, возвращает один фильм, самый свежий
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        movie_data = cursor.execute("SELECT * FROM 'netflix' WHERE 'title'=? ORDER BY 'release_year' LIMIT 1", (movie_title))
        movie_data_form = {"title" = movie_data["title"], "country" = movie_data["country"], "release_year" = movie_data["release_year"], "genre" = movie_data["listed_in"], "description" = movie_data["description"]}
        return movie_data_form


def search_by_date(start_date, end_date : str) -> list[dict]:
    """
    Поиск в базе данных по диапазону лет выпуска, возвращает 100 записей
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        movie_data = cursor.execute("SELECT 'title', 'release_date' FROM 'netflix' WHERE 'release_date' BETWEEN ? AND ? ORDER BY 'release_year' LIMIT 100", (start_date, end_date))
        for movie in movie_data:
            movie_form = {"title" = movie["title"], "release_year" = movie["release_year"]}
            movie_data_form += movie_form
        return movie_data_form


def search_by_children_rating() -> list[dict]:
    """
    Поиск в базе данных по детскому рейтингу, возвращает 100 записей
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        movie_data = cursor.execute("SELECT 'title', 'rating', 'description' FROM 'netflix' WHERE 'rating' LIKE 'G' LIMIT 100")
        for movie in movie_data:
            movie_form = {"title" = movie["title"], "rating" = movie["rating"], "description" = movie["description"]}
            movie_data_form += movie_form
        return movie_data_form


def search_by_family_rating() -> list[dict]:
    """
    Поиск в базе данных по семейному рейтингу, возвращает 100 записей
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        movie_data = cursor.execute("SELECT 'title', 'rating', 'description' FROM 'netflix' WHERE 'rating' LIKE 'G' OR 'rating' LIKE 'PG' OR 'rating' LIKE 'PG-13' LIMIT 100")
        for movie in movie_data:
            movie_form = {"title" = movie["title"], "rating" = movie["rating"], "description" = movie["description"]}
            movie_data_form += movie_form
        return movie_data_form


def search_by_adult_rating() -> list[dict]:
    """
    Поиск в базе данных по взрослому рейтингу, возвращает 100 записей
    """
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        movie_data = cursor.execute("SELECT 'title', 'rating', 'description' FROM 'netflix' WHERE 'rating' LIKE 'R' OR 'rating' LIKE 'NC-17' LIMIT 100")
        for movie in movie_data:
            movie_form = {"title" = movie["title"], "rating" = movie["rating"], "description" = movie["description"]}
            movie_data_form += movie_form
        return movie_data_form




test_data = search_by_title("zozo")
print(test_data)