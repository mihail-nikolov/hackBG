from create_cinema import Projection, Movie, Reservation


class Cinema():

    def __init__(self, session):
        self.session = session
        self.hall_rows = 10
        self.hall_cols = 10
        self._make_halls()

    def _make_halls(self):
        self.proj_halls = {}
        result = self.session.query(Projection).all()
        for el in result:
            matrix = []
            for i in range(self.hall_rows):
                array = []
                for j in range(self.hall_cols):
                    array.append(".")
                matrix.append(array)
            self.proj_halls[el.id] = matrix

    def add_movie(self, m_name, m_rating):
        self.session.add(Movie(name=m_name, rating=m_rating))
        self.session.commit()

    def show_movies(self):
        movies = self.session.query(Movie).all()
        return movies

    def make_reservation(self, name, places_arr, proj_id):
        for place in places_arr:
            self.session.add(Reservation(username=name, projection_id=proj_id, row=place[0], col=place[1]))
            self.session.commit()

    def cancel_reservation(self, name):
        self.session.delete(Reservation.username == name)
        self.conn.commit()

    def clear_reservation_on_startup(self):
        #!!!!!!!!!!!!!!
        self.session.delete(Reservation.objects.all())
        self.session.commit()

    def add_projection(self, m_id, m_type, m_date, time):
        self.session.add(Projection(movie_id=m_id, movie_type=m_type, movie_date=m_date, movie_time=time))
        self.session.commit()

    def show_movie_projection(self, m_id):
        result = self.session.query(Projection).filter(Projection.movie_id == m_id).all()
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
        proj = self.session.query(Projection).filter(Projection.id == proj_id).one()
        return proj.movie_date, proj.movie_time

    def _get_movie_name(self, m_id):
        m_id = int(m_id)
        movies = self.session.query(Movie).filter(Movie.id == m_id).one()
        return movies.name
