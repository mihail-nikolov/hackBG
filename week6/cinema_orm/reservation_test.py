import unittest
from reservation import Reservation


class Projections_test(unittest.TestCase):

    def test_add_reservation(self):
        db = "cinema.db"
        reservation = Reservation(db)
        places = [[2, 3], [2, 2]]
        #reservation.make_reservation("Misho", places, 2)
        #reservation.cancel_reservation("Misho")

if __name__ == '__main__':
    unittest.main()
