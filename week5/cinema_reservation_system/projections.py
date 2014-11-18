import sqlite3


class Projections():

    def __init__(self, db):
        conn = sqlite3.connect(db)
        self.conn = conn
        cursor = conn.cursor()
        self.cursor = cursor

    def add_projection(self, movie_id, type, movie_date, time):
        self.cursor.execute("""INSERT INTO Projections
                            (movie_id, type, movie_date, time)
                            VALUES(?, ?, ?, ?)""",
                            (movie_id, type, movie_date, time))
        self.conn.commit()

    def show_movie_projection(self, movie_id):
        result = self.cursor.execute('''SELECT id, type,
                                 movie_date, time FROM Projections
                                WHERE movie_id = ? ''', (movie_id, ))
        for row in result:
            print(row)
