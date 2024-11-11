import math
import unittest

from mean import arithmetic_mean, geometric_mean, mean

class TestMean(unittest.TestCase):
    """Test the mean module."""
    
    def test_arithmetic_mean(self):
        """Test the arithmetic_mean function."""
        self.assertEqual(arithmetic_mean([7]), 7)
        self.assertEqual(arithmetic_mean([2.34, -2.34]), 0)
        self.assertAlmostEqual(arithmetic_mean([1, 2, 3, 4, 5]), 3.0)

    def test_arithmetic_mean_empty(self):
        """Test the arithmetic_mean function with an empty sequence."""
        with self.assertRaises(ValueError) as context:
            arithmetic_mean([])
        self.assertEqual(str(context.exception), "The sequence is empty")

    def test_geometric_mean(self):
        """Test the geometric_mean function."""
        self.assertEqual(geometric_mean([1, 1, 1, 1, 1]), 1)
        self.assertAlmostEqual(geometric_mean([2, 2, 2, 2, 2]), 2.0)

    def test_geometric_mean_empty(self):
        """Test the geometric_mean function with an empty sequence."""
        with self.assertRaises(ValueError) as context:
            geometric_mean([])
        self.assertEqual(str(context.exception), "The sequence is empty")

    def test_mean(self):
        """Test the mean function."""
        self.assertAlmostEqual(mean([1, 2, 3, 4, 5], "arithmetic"), 3.0)
        self.assertAlmostEqual(
            mean([1, 2, 3, 4, 5], "geometric"), (1 * 2 * 3 * 4 * 5) ** (1 / 5)
        )

    def test_mean_empty(self):
        """Test the mean function with an empty sequence."""
        with self.assertRaises(ValueError) as context:
            mean([], "arithmetic")
        self.assertEqual(str(context.exception), "The sequence is empty")

        with self.assertRaises(ValueError) as context:
            mean([], "geometric")
        self.assertEqual(str(context.exception), "The sequence is empty")

    def test_mean_incorrect_type(self):
        """Test the mean function with an incorrect mean type."""
        with self.assertRaises(ValueError) as context:
            mean([1, 2, 3, 4, 5], "abc")
        self.assertEqual(str(context.exception), "Incorrect type of mean")

    def test_mean_default_type(self):
        """Test the mean function with the default mean type."""
        self.assertAlmostEqual(mean([1, 2, 3, 4, 5]), 3.0)
        
if __name__ == "__main__":
    unittest.main()