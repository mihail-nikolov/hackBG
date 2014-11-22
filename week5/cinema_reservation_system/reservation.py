import sqlite3


class Reservation():

    def __init__(self, db):
        conn = sqlite3.connect(db)
        self.conn = conn
        cursor = conn.cursor()
        self.cursor = cursor

    def make_reservation(self, name, places_arr, proj_id):
        for place in places_arr:
            self.cursor.execute("""INSERT INTO Reservations
                            (username, projection_id, row, col)
                            VALUES(?, ?, ?, ?)""",
                            (name, proj_id, int(place[0]), int(place[1])))
            self.conn.commit()

    def show_reservations(self, movie_id):
        result = self.cursor.execute('''SELECT * FROM reservations''')
        for row in result:
            print(row)

    def cancel_reservation(self, name):
        self.cursor.execute("""DELETE FROM Reservations WHERE username = ?""",
                                                                      (name,))
        self.conn.commit()

    def clear_reservation_on_stratup(self):
        self.cursor.execute("""DELETE FROM Reservations""")
        self.conn.commit()
