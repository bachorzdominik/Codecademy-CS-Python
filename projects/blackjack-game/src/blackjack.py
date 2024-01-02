import random


class NoCardsRemainingError(Exception):
	pass


class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.is_face_up = True

	def __repr__(self):
		if self.is_face_up:
			return f'{self.rank} of {self.suit}'
		else:
			return 'Card is face down'

	def flip(self):
		self.is_face_up = not self.is_face_up
		return self.is_face_up


class Deck:
	def __init__(self):
		self.cards = []
		self.num_cards = 0
		self.create_deck()

	def create_deck(self):
		suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
		ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

		for suit in suits:
			for rank in ranks:
				self.cards.append(Card(suit, rank))
				self.num_cards += 1

	def shuffle_deck(self):
		random.shuffle(self.cards)

	def deal_card(self):
		if self.num_cards > 0:
			self.num_cards -= 1
			return self.cards.pop()
		else:
			raise NoCardsRemainingError('The deck is empty. Cannot deal a card.')
		
	def get_num_cards(self):
		return self.num_cards


class Player:
	def __init__(self, name):
		self.name = name
		self.hand = []
		self.score = 0

	def __repr__(self):	
		return f'{self.name} has {self.hand} with a score of {self.score}'
	
	def add_card_to_hand(self, card):
		self.hand.append(card)
		self.calculate_score()

	def calculate_score(self):
		score = 0
		aces = 0
		for card in self.hand:
			if card.rank == 'Ace':
				aces += 1
				score += 11
			elif card.rank in ['Jack', 'Queen', 'King']:
				score += 10
			else:
				score += int(card.rank)

		while score > 21 and aces:
			score -= 10
			aces -= 1

		self.score = score


class BlackjackGame:
	def __init__(self):
		self.players = []
		self.deck = Deck()
		self.dealer = Player('Dealer')

	def add_player(self, player):
		self.players.append(player)

	def remove_player(self, player):
		self.players.remove(player)
	
	def deal_initial_cards(self):
		for _ in range(2): # deal 2 cards to each player and the dealer
			for player in [self.dealer] + self.players:
				card = self.deck.deal_card()
				player.add_card_to_hand(card)

	def play_round(self):
		self.deck.shuffle_deck()
		self.deal_initial_cards()

		for player in self.players:
			print(f'{player.name}\'s turn: {player.hand}')
			player.calculate_score()
			print(f'{player.name}\'s score: {player.score}\n')

		print(f'Dealer\'s turn: {self.dealer.hand[0]}')
		self.dealer.calculate_score()
		print(f'Dealer\'s score: {self.dealer.score}\n')

		for player in self.players:
			while player.score < 21:
				choice = input(f'{player.name}, would you like to hit or stand? (h/s): ').lower()
				if choice == 'h':
					card = self.deck.deal_card()
					player.add_card_to_hand(card)
					player.calculate_score()

					print(f'{player.name}\'s hand: {player.hand}')
					print(f'{player.name}\'s score: {player.score}\n')
				elif choice == 's':
					break
			
			while self.dealer.score < 17:
				card = self.deck.deal_card()
				self.dealer.add_card_to_hand(card)
				self.dealer.calculate_score()

				print(f'Dealer\'s hand: {self.dealer.hand}')
				print(f'Dealer\'s score: {self.dealer.score}\n')

		for player in self.players:
			if player.score > 21:
				print(f'{player.name} busted! You lose!')
			elif self.dealer.score > 21 or player.score > self.dealer.score:
				print(f'{player.name} beat the dealer! You win!')
			elif self.dealer.score == player.score:
				print(f'{player.name} tied with the dealer! You tie!')
			else:
				print(f'{player.name} lost to the dealer! You lose!')


blackjack_game = BlackjackGame()
blackjack_game.add_player(Player('John'))
blackjack_game.add_player(Player('Jane'))

blackjack_game.play_round()
