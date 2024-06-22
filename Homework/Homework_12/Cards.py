from random import shuffle as random_array


class Card:
    number_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    mast_list = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
    jocker_list = [('Red', 'Jocker'), ('Black', 'Jocker')]

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __str__(self):
        return f'{self.mast} {self.number}'


class CardsDeck:

    def __init__(self):
        card_array = []
        for mast in Card.mast_list:
            for number in Card.number_list:
                card_array.append(Card(number, mast))
        for mast, number in Card.jocker_list:
            card_array.append(Card(number, mast))
        self.deck = card_array

    def shuffle(self):
        random_array(self.deck)

    def get(self, number):
        if number < len(self.deck):
            return self.deck[number]
        return None


deck = CardsDeck()
deck.shuffle()
card_number = int(input('Выберите карту из колоды в 54 карты:'))
card = deck.get(card_number)
print(f'You card is: {card}')
