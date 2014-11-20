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
        #res_arr = []
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
        is_in_range = col <= self.hall_cols and row <= self.hall_rows
        is_free = hall[row][col] == "."
        if is_free and is_in_range:
            return True
        return False

    def write_x(self, proj_id, place):
        row = place[0] - 1
        col = place[1] - 1
        self.proj_halls[proj_id][row][col] = "X"




db = "cinema.db"
proj = Projections(db)
proj._make_halls()
print(proj.is_there_place(2, 2))
print(proj.proj_halls[1])
