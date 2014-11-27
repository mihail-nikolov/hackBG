import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from cinema import Cinema


engine = create_engine("sqlite:///cinema.db")
session = Session(bind=engine)

cinema = Cinema(session)


class Create_cinema_test(unittest.TestCase):

    def test_get_date_time(self):
        result = cinema._get_movie_date_time(1)
        self.assertEqual(result, ("2014-04-01", "19:10"))

    def test_get_movie_name(self):
        movie = cinema._get_movie_name(1)
        self.assertEqual(movie, "The Hunger Games: Catching Fire")
if __name__ == '__main__':
    unittest.main()
