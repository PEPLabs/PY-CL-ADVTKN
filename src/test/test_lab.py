import unittest
from src.main.lab import stemmingExercise, lemmatizingExercise

class TestAdvTknExercises(unittest.TestCase):
    def test_stemming_exercise(self):
        result = stemmingExercise()

        self.assertGreaterEqual(len(result), 10)
        self.assertTrue('discoveri' in result)

    def test_lemmatizing_exercise(self):
        result = lemmatizingExercise()
        print(result)
        self.assertGreaterEqual(len(result), 10)
        self.assertTrue('race' in result)

if __name__ == '__main__':
    unittest.main()