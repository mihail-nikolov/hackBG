import sqlite3
from create_table import Player


class Game():

    def __init__(self, session, db):
        self.session = session
        self.db = db
        conn = sqlite3.connect(db)
        self.conn = conn
        cursor = conn.cursor()
        self.cursor = cursor

    def add_user(self, name, result, points):
        self.session.add(Player(name=name, result=result, points=points))
        self.session.commit()

    def get_rating_table(self):
        result = self.cursor.execute('''SELECT name, points FROM players
                                               ORDER BY points''').fetchall()
        return result

    def _get_result(self, name):
        player = self.session.query(Player).filter(Player.name == name).all()
        return player[0].result

    def _increase_result(self, name):
        self.cursor.execute('''UPDATE players SET result = result + 1
                    WHERE name = ? ''', (name, ))
        self.conn.commit()

    def calculate_points(self, name, result):
        calc_points = result * result
        self.cursor.execute('''UPDATE players SET points = ?
                    WHERE name = ? ''', (calc_points, name))
        self.conn.commit()
        return calc_points
