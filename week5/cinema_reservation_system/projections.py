import sqlite3


class Projections():

    def __init__(self, db):
        conn = sqlite3.connect(db)
        self.conn = conn
        cursor = conn.cursor()
        self.cursor = cursor
        self.hall_rows = 10
        self.hall_cols = 10
        self._make_halls()

    def _make_halls(self):
        self.proj_halls = {}
        result = self.cursor.execute('''SELECT id FROM Projections''').fetchall()
        for el in result:
            matrix = []
            for i in range(self.hall_rows):
                array = []
                for j in range(self.hall_cols):
                    array.append(".")
                matrix.append(array)
            self.proj_halls[el[0]] = matrix

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
        return result

    def is_there_place(self, proj_id, tickets):
        tickets = int(tickets)
        proj_id = int(proj_id)
        avlb_places = 0
        the_hall = self.proj_halls[proj_id]
        for row in the_hall:
            for col in row:
                if col == ".":
                    avlb_places += 1
        if avlb_places >= tickets:
            return True
        return False

    def is_place_OK(self, proj_id, place):
        proj_id = int(proj_id)
        row = place[0] - 1
        col = place[1] - 1
        hall = self.proj_halls[proj_id]
        a_row_len = len(self.proj_halls[1][0])
        a_col_len = len(self.proj_halls[1])
        is_in_range = col in range(a_col_len) and row in range(a_row_len)
        if is_in_range:
            if hall[row][col] == ".":
                return True
        return False

    def write_x(self, proj_id, place):
        proj_id = int(proj_id)
        row = int(place[0] - 1)
        col = int(place[1] - 1)
        self.proj_halls[proj_id][row][col] = "X"

    def del_x(self, proj_id, places_arr):
        proj_id = int(proj_id)
        for place in places_arr:
            row = int(place[0] - 1)
            col = int(place[1] - 1)
            self.proj_halls[proj_id][row][col] = "."

    def _get_movie_date_time(self, proj_id):
        proj_id = int(proj_id)
        result = self.cursor.execute('''SELECT movie_date, time
                                FROM Projections
                                WHERE id = ? ''', (proj_id, )).fetchall()
        return result[0][0], result[0][1]
