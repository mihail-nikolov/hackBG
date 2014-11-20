import sqlite3


class Reservation():

    def __init__(self, db):
        conn = sqlite3.connect(db)
        self.conn = conn
        cursor = conn.cursor()
        self.cursor = cursor

    def make_reservation(self, movie_id, type, movie_date, time):
        self.cursor.execute("""INSERT INTO Reservations
                            (movie_id, type, movie_date, time)
                            VALUES(?, ?, ?, ?)""",
                            (movie_id, type, movie_date, time))
        self.conn.commit()

    def show_reservations(self, movie_id):
        result = self.cursor.execute('''SELECT * FROM reservations''')
        for row in result:
            print(row)

    def cancel_reservation(name):
        pass
