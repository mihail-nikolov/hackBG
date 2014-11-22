import sqlite3


class Movies():

    def __init__(self, db):
        conn = sqlite3.connect(db)
        self.conn = conn
        cursor = conn.cursor()
        self.cursor = cursor

    def add_movie(self, name, rating):
        self.cursor.execute("""INSERT INTO  Movies(name, rating)
                             VALUES(?, ?)""", (name, rating))
        self.conn.commit()

    def show_movies(self):
        result = self.cursor.execute('''SELECT * FROM Movies
                                               ORDER BY rating''')
        return result

    def _get_movie_name(self, movie_id):
        movie_id = int(movie_id)
        result = self.cursor.execute('''SELECT name FROM Movies
                                        WHERE id = ?''', (movie_id,)).fetchone()
        return result[0]
