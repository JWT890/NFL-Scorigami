import unittest
from scorigami import get_scorigami_scores

class TestGetScorigamiScores(unittest.TestCase):
    def test_get_scorigami_scores(self):
        # Call the function
        scores = get_scorigami_scores()

        # Assert that the returned value is not empty
        self.assertIsNotNone(scores)

        # Assert that the returned value is a set
        self.assertIsInstance(scores, set)

        # Assert that the set contains integers
        for score in scores:
            self.assertIsInstance(score, int)

if __name__ == '__main__':
    unittest.main()