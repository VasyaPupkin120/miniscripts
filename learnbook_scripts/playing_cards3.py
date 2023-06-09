"""
Набранный пример из книги, классы карт, руки, колоды для дальнейшего использования. 
Самостоятельного функционала модуль не имеет.
"""
class Card():
    """Одна карта"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",]
    # c - clubs (трефы, деревце), d-diamonds (бубны), h-hearts(червы), s-spades(пики, сердце на палке)
    SUITS = ["c", "d", "h", "s",]
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        rep = self.rank + self.suit
        return rep


class Unprintable_Card(Card):
    """у этой карты номинал и масть не могут быть выведены на экран"""
    def __repr__(self):
        return "<нельзя напечатать>"


class Positionable_Card(Card):
    """эту карту можно положить лицом или рубашкой вверх"""

    def __init__(self, rank, suit, face_up=True) -> None:
        super().__init__(rank, suit)
        self.is_face_up = face_up
    
    def __repr__(self) -> str:
        if self.is_face_up:
            rep = super().__repr__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up



class Hand():
    """Рука: набор карт на руках одного игрока"""

    def __init__(self) -> None:
        self.cards = []

    def __repr__(self) -> str:
        if self.cards:
            rep = ""
            for card  in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<пусто>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """Колода карт"""

    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        """раздача карт"""
        for rounds in range(per_hand):
            for hand  in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Не могу раздавать: карты закончилсь.")


def main():
    card1 = Card("A", "c")
    card2 = Unprintable_Card("A", "d")
    card3 = Positionable_Card("A", "h")
    print("card1", card1)
    print("card2", card2)
    print("card3", card3)
    card3.flip()
    print("переворачиваем card3", card3)


if __name__ == "__main__":
    main()

