import unittest
from projections import Projections


class Projections_test(unittest.TestCase):

    def test_add_projection(self):
        db = "cinema.db"
        projections = Projections(db)
        #projections.add_projection(1, "3D", "2014-04-01", "19:10")
        #projections.add_projection(1, "2D", "2014-04-01", "19:00")
        #projections.add_projection(1, "4DX", "2014-04-02", "21:00")
        #projections.add_projection(3, "2D", "2014-04-05", "20:00")
        #projections.add_projection(2, "3D", "2014-04-02", "22:00")
        #projections.add_projection(2, "2D", "2014-04-02", "19:30")
        #TESTING SHOW PROJECTIONS
        projections.show_movie_projection(2)

if __name__ == '__main__':
    unittest.main()
