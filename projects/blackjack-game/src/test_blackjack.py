import unittest
from blackjack import Card, Deck, NoCardsRemainingError, Player

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card('Hearts', 'Ace')

    def test_flip(self):
        self.assertTrue(self.card.is_face_up)
        self.card.flip()
        self.assertFalse(self.card.is_face_up)

    def test_repr(self):
        self.assertEqual(repr(self.card), 'Ace of Hearts')
        self.card.flip()
        self.assertEqual(repr(self.card), 'Card is face down')


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_create_deck(self):
        self.assertEqual(self.deck.get_num_cards(), 52)
        self.assertIsInstance(self.deck.cards[0], Card)

    def test_shuffle_deck(self):
        cards_before_shuffle = self.deck.cards[:]
        self.deck.shuffle_deck()
        self.assertNotEqual(self.deck.cards, cards_before_shuffle)

    def test_deal_card(self):
        initial_num_cards = self.deck.get_num_cards()
        dealt_card = self.deck.deal_card()
        self.assertIsInstance(dealt_card, Card)
        self.assertEqual(self.deck.get_num_cards(), initial_num_cards - 1)

    def test_no_cards_remaining(self):
        for _ in range(52):
            self.deck.deal_card()
        with self.assertRaises(NoCardsRemainingError):
            self.deck.deal_card()


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player('John')
        self.card1 = Card('Hearts', 'Ace')
        self.card2 = Card('Spades', 'Ace')

    def test_init(self):
        self.assertEqual(self.player.name, 'John')
        self.assertEqual(self.player.hand, [])
        self.assertEqual(self.player.score, 0)

    def test_repr(self):
        self.assertEqual(repr(self.player), 'John has [] with a score of 0')

    def test_add_card_to_hand(self):
        self.player.add_card_to_hand(self.card1)
        self.assertEqual(self.player.hand, [self.card1])

    def test_calculate_score(self):
        self.player.add_card_to_hand(self.card1)
        self.player.calculate_score()
        self.assertEqual(self.player.score, 11)
        self.player.add_card_to_hand(self.card2)
        self.player.calculate_score()
        self.assertEqual(self.player.score, 12)


if __name__ == '__main__':
    unittest.main()
