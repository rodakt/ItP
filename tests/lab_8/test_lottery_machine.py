"""Tests for lottery_machine."""
import unittest

try:
    from lottery_machine import lottery_machine
except ImportError:
    raise SystemExit('Could not find lottery_machine.py. Does it exist?')


class LotteryMachineTests(unittest.TestCase):
    """Tests for lottery_machine."""

    def test_draw_all_balls_without_replacement(self):
        """All six balls are drawn, then the urn is empty."""
        lottery = lottery_machine(replacement=False, red=2, blue=3, green=1)
        for i in range(5):
            self.assertEqual(len(lottery()), i + 1)
        self.assertEqual(sorted(lottery()),
                         ['blue', 'blue', 'blue', 'green', 'red', 'red'])
        with self.assertRaises(LookupError):
            lottery()

    def test_draw_1000_balls_with_replacement(self):
        """1000 balls are drawn with replacement."""
        lottery = lottery_machine(red=2, blue=3, green=1)
        for i in range(1000):
            self.assertEqual(len(lottery()), i + 1)
        drawn = lottery()
        self.assertEqual(set(drawn), {'red', 'blue', 'green'})
        self.assertGreater(drawn.count('blue'), drawn.count('green'))

    def test_previous_draws_are_kept(self):
        """Each call extends the list returned by the previous one."""
        lottery = lottery_machine(red=1, blue=1)
        previous = lottery()
        for _ in range(20):
            current = lottery()
            self.assertEqual(current[:-1], previous)
            previous = current

    def test_returns_new_list(self):
        """Changing the returned list does not affect the machine."""
        lottery = lottery_machine(red=1)
        drawn = lottery()
        drawn.append('blue')
        self.assertEqual(lottery(), ['red', 'red'])

    def test_empty_urn_message(self):
        """The message of the exception is 'The urn is empty'."""
        lottery = lottery_machine(replacement=False, red=1)
        lottery()
        with self.assertRaises(LookupError) as context:
            lottery()
        self.assertEqual(str(context.exception), 'The urn is empty')

    def test_urn_empty_from_start(self):
        """An urn without balls is empty, with or without replacement."""
        for replacement in [True, False]:
            for lottery in [lottery_machine(replacement=replacement),
                            lottery_machine(replacement=replacement, red=0)]:
                with self.assertRaises(LookupError):
                    lottery()

    def test_zero_quantity_colour_is_never_drawn(self):
        """A colour with quantity 0 is never drawn."""
        lottery = lottery_machine(red=0, blue=1)
        for _ in range(100):
            drawn = lottery()
        self.assertEqual(set(drawn), {'blue'})

    def test_negative_quantity(self):
        """A negative quantity raises ValueError at once."""
        with self.assertRaises(ValueError):
            lottery_machine(red=2, blue=-1)

    def test_machines_are_independent(self):
        """Two machines do not share their urns or their draws."""
        first = lottery_machine(replacement=False, red=1)
        second = lottery_machine(replacement=False, red=1)
        self.assertEqual(first(), ['red'])
        self.assertEqual(second(), ['red'])
        with self.assertRaises(LookupError):
            first()


if __name__ == "__main__":
    unittest.main()
