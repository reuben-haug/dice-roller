import unittest
from unittest.mock import patch
from Dice.input import get_user_input

class TestUserInput(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '6', '10'])
    def test_get_user_input(self, input):
        dice, sides, rolls = get_user_input()
        self.assertEqual(dice, 2)
        self.assertEqual(sides, 6)
        self.assertEqual(rolls, 10)

if __name__ == '__main__':
    unittest.main()
