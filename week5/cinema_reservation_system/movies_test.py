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

if __name__ == '__main__':
    unittest.main()
