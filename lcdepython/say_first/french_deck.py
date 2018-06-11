import collections

#用以构建只有少数属性但是没有方法的对象，比如数据库条目。
# nametuple返回一个类名为Card的tuple的子类
#这里表示一张纸牌类
Card = collections.namedtuple('Card', ['rank', 'suit'])
beer_card = Card('7', 'diamonds')
print(beer_card.rank) # 7
print(beer_card.suit) # diamonds

class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split() # 黑桃，方块，梅花， 红桃

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

deck = FrenchDeck()
print(len(deck)) # 52

print(deck[0]) # Card(rank='2', suit='spades')
print(deck[-1]) # Card(rank='A', suit='hearts')

from random import choice # choice(seq)
'''    def choice(self, seq):
        """Choose a random element from a non-empty sequence."""
            i = self._randbelow(len(seq))
        return seq[i]'''
# 还是调用了__getitem__
print(choice(deck)) # Card(rank='K', suit='clubs')
print(choice(deck)) # Card(rank='7', suit='hearts')
print(deck.__dict__["_cards"].pop())