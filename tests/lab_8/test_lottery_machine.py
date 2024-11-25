"""Tests for lottery_machine."""
import unittest
import random

try:
    from lottery_machine import lottery_machine
except ImportError:
    raise SystemExit('Could not find lottery_machine.py. Does it exist?')

class LotteryMachineTests(unittest.TestCase):
    """Tests for lottery_machine."""
    
    def test_draw_five_balls_without_replacement(self):
        """Test that five balls are drawn without replacement."""
        balls = {'red': 2, 'blue': 3, 'green': 1}
        lottery = lottery_machine(replacement=False, **balls)
        for i in range(5):
            self.assertEqual(len(lottery()), i + 1)
        self.assertEqual(sorted(lottery()), ['blue', 'blue', 'blue', 'green', 'red', 'red'])
        with self.assertRaises(LookupError):
            lottery()
    
    def test_draw_1000_balls_with_replacement(self):
        """Test that 1000 balls are drawn with replacement."""
        balls = {'red': 2, 'blue': 3, 'green': 1}
        lottery = lottery_machine(**balls)
        for i in range(1000):
            self.assertEqual(len(lottery()), i + 1)
        lst = lottery()
        self.assertGreater(lst.count('blue'), lst.count('green'))
        
if __name__ == "__main__":
    unittest.main()