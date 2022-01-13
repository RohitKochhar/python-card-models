from random import shuffle

class Card:
    a_Suites    = ["SPADE", "CLUB", "HEART", "DIAMOND"]
    a_Ranks     = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]
    def __init__(self, i_ID):
        self.i_ID       = i_ID
        self.i_Rank     = i_ID % 13
        self.i_Suite    = int(i_ID / 13)

    def getRank(self):
        return self.i_Rank

    def getSuite(self):
        return self.i_Suite

    def getRankLiteral(self):
        return self.a_Ranks[self.i_Rank]

    def getSuiteLiteral(self):
        return self.a_Suites[self.i_Suite]

    def __str__(self):
        return f"Card ID{self.i_ID} -> the {self.getRankLiteral()} of {self.getSuiteLiteral()}S"

class Deck:
    a_Cards         = []
    a_DrawnCards    = []

    def __init__(self):
        for i in range(0, 52):
            self.a_Cards.append(Card(i))

    def shuffle(self):
        shuffle(self.a_Cards)

    def reset(self):
        self.__init__()

    def drawCard(self):
        o_DrawnCard = self.a_Cards.pop(0)
        self.a_DrawnCards.append(o_DrawnCard)
        return o_DrawnCard



o_TestDeck = Deck()
o_TestDeck.shuffle()
o_TestDeck.reset()
for card in o_TestDeck.a_Cards:
    print(card)
