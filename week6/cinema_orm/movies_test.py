import unittest
from movies import Movies


class Movies_test(unittest.TestCase):

    def test_add_movie(self):
        db = "cinema.db"
        movies = Movies(db)
        #movies.add_movie("The Hunger Games: Catching Fire", 7.9)
        #movies.add_movie("Wreck-It Ralph", 7.8)
        #movies.add_movie("Her", 8.3)
        #TESTING SHOW MOVIES
        movies.show_movies()

    def test_get_movie_name(self):
        db = "cinema.db"
        movies = Movies(db)
        movie = movies._get_movie_name(1)
        self.assertEqual(movie, "The Hunger Games: Catching Fire")


if __name__ == '__main__':
    unittest.main()
