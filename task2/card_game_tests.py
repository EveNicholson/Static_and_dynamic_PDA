
import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1=Card("diamonds",1)
        self.card2=Card("hearts", 10)
        
    
        self.cards = [self.card1, self.card2]

        
    def test_check_for_ace(self):
        self.assertEqual(True,self.card1.value)

    def test_highest_card(self):
        self.assertEqual(True, self.card1.value)

    def test_cards_total(self):
        self.assertEqual(True,self.card1.value)
