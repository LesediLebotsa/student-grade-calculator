import unittest
from calculations import calculate_grade


class TestCalculations(unittest.TestCase):
    def test_normal_marks(self):

        result = calculate_grade(
            80,
            70,
            90,
            85
        )

        self.assertEqual(
            result,
            84.0
        )

    def test_zero_marks(self):

        result = calculate_grade(
            0,
            0,
            0,
            0
        )

        self.assertEqual(
            result,
            0
        )

    def test_full_marks(self):

        result = calculate_grade(
            100,
            100,
            100,
            100
        )

        self.assertEqual(
            result,
            100
        )

if __name__ == "__main__":
    unittest.main()