import unittest
from scorigami import is_scorigami

def test_is_scorigami():
    # Define a set of scorigami scores
    scorigami_scores = {3, 7, 10, 14, 17}

    # Test case 1: Scorigami score (not in the set)
    home_score = 20
    away_score = 13
    assert is_scorigami(home_score, away_score, scorigami_scores) == True

    # Test case 2: Non-scorigami score (in the set)
    home_score = 7
    away_score = 14
    assert is_scorigami(home_score, away_score, scorigami_scores) == False

    # Test case 3: Scorigami score (not in the set)
    home_score = 17
    away_score = 0
    assert is_scorigami(home_score, away_score, scorigami_scores) == True

if __name__ == "__main__":
    unittest.main()