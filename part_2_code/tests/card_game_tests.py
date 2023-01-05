import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card ("hearts", 1)
        self.card2 = Card ("diamonds", 6)
        self.card_game = CardGame()

    def test_check_for_ace_true(self):
        result = self.card_game.check_for_ace(self.card1)
        self.assertEqual(True, result)

    def test_check_for_ace_false(self):
        result = self.card_game.check_for_ace(self.card2)
        self.assertEqual(False, result)

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2.value, result.value)

    def test_cards_total (self):
        cards = self.card1, self.card2
        result = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 7", result)
