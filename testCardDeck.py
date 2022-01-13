from CardDeck import Card, Deck

def test_blank_constructor():
    o_Card = Card()

def test_spade_assignment():
    for i in range(0, 12):
        o_TestCard  = Card(i)
        assert o_TestCard.getSuit() == 0, f"ID: {i} - Expected a Suit of 0, got {o_TestCard.getSuit()} instead"
        assert o_TestCard.getSuitLiteral() == "SPADE", f"ID: {i} - Expected a Suit of SPADE, got {o_TestCard.getSuitLiteral()} instead"

def test_club_assignment():
    for i in range(13, 25):
        o_TestCard  = Card(i)
        assert o_TestCard.getSuit() == 1, f"ID: {i} - Expected a Suit of 1, got {o_TestCard.getSuit()} instead"
        assert o_TestCard.getSuitLiteral() == "CLUB", f"ID: {i} - Expected a Suit of CLUB, got {o_TestCard.getSuitLiteral()} instead"

def test_heart_assignment():
    for i in range(26, 38):
        o_TestCard  = Card(i)
        assert o_TestCard.getSuit() == 2, f"ID: {i} - Expected a Suit of 2, got {o_TestCard.getSuit()} instead"
        assert o_TestCard.getSuitLiteral() == "HEART", f"ID: {i} - Expected a Suit of HEART, got {o_TestCard.getSuitLiteral()} instead"


def test_diamond_assignment():
    for i in range(39, 52):
        o_TestCard  = Card(i)
        assert o_TestCard.getSuit() == 3, f"ID: {i} - Expected a Suit of 3, got {o_TestCard.getSuit()} instead"
        assert o_TestCard.getSuitLiteral() == "DIAMOND", f"ID: {i} - Expected a Suit of DIAMOND, got {o_TestCard.getSuitLiteral()} instead"

def test_all_card_assignment():
    for i in range(0, 52):
        o_TestCard = Card(i)
        if i <= 12:
            assert o_TestCard.getSuit() == 0, f"ID: {i} - Expected a Suit of 0, got {o_TestCard.getSuit()} instead"
            assert o_TestCard.getSuitLiteral() == "SPADE", f"ID: {i} - Expected a Suit of SPADE, got {o_TestCard.getSuitLiteral()} instead"
            assert o_TestCard.getRank()  == i, f"ID: {i} - Expected a rank of {i}, got {o_TestCard.getRank()} instead"
        if i > 13 and i <= 25:
            assert o_TestCard.getSuit() == 1, f"ID: {i} - Expected a Suit of 1, got {o_TestCard.getSuit()} instead"
            assert o_TestCard.getSuitLiteral() == "CLUB", f"ID: {i} - Expected a Suit of CLUB, got {o_TestCard.getSuitLiteral()} instead"
            assert o_TestCard.getRank()  == i - 13, f"ID: {i} - Expected a rank of {i - 13}, got {o_TestCard.getRank()} instead"        
        if i > 26 and i <= 38:
            assert o_TestCard.getSuit() == 2, f"ID: {i} - Expected a Suit of 2, got {o_TestCard.getSuit()} instead"
            assert o_TestCard.getSuitLiteral() == "HEART", f"ID: {i} - Expected a Suit of HEART, got {o_TestCard.getSuitLiteral()} instead"
            assert o_TestCard.getRank()  == i - 26, f"ID: {i} - Expected a rank of {i - 26}, got {o_TestCard.getRank()} instead"  
        if i > 39 and i <= 51:
            assert o_TestCard.getSuit() == 3, f"ID: {i} - Expected a Suit of 3, got {o_TestCard.getSuit()} instead"
            assert o_TestCard.getSuitLiteral() == "DIAMOND", f"ID: {i} - Expected a Suit of DIAMOND, got {o_TestCard.getSuitLiteral()} instead"
            assert o_TestCard.getRank()  == i - 39, f"ID: {i} - Expected a rank of {i - 39}, got {o_TestCard.getRank()} instead" 

def test_ace_of_spades():
    id = 0
    o_TestCard = Card(id)
    assert o_TestCard.getSuit() == 0, f"ID: {id} - Expected a Suit of 0, got {o_TestCard.getSuit()} instead"
    assert o_TestCard.getSuitLiteral() == "SPADE", f"ID: {id} - Expected a Suit of SPADE, got {o_TestCard.getSuitLiteral()} instead"
    assert o_TestCard.getRank()  == 0, f"ID: {0} - Expected a rank of 0, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "ACE", f"ID: {0} - Expected a rank of ACE, got {o_TestCard.getRank()} instead"

def test_ace_of_clubs():
    id = 0 + 13
    o_TestCard = Card(id)
    assert o_TestCard.getSuit() == 1, f"ID: {id} - Expected a Suit of 1, got {o_TestCard.getSuit()} instead"
    assert o_TestCard.getSuitLiteral() == "CLUB", f"ID: {id} - Expected a Suit of CLUB, got {o_TestCard.getSuitLiteral()} instead"
    assert o_TestCard.getRank()  == 0, f"ID: {0} - Expected a rank of 0, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "ACE", f"ID: {0} - Expected a rank of ACE, got {o_TestCard.getRank()} instead"

def test_ace_of_hearts():
    id = 0 + 26
    o_TestCard = Card(id)
    assert o_TestCard.getSuit() == 2, f"ID: {id} - Expected a Suit of 2, got {o_TestCard.getSuit()} instead"
    assert o_TestCard.getSuitLiteral() == "HEART", f"ID: {id} - Expected a Suit of HEART, got {o_TestCard.getSuitLiteral()} instead"
    assert o_TestCard.getRank()  == 0, f"ID: {0} - Expected a rank of 0, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "ACE", f"ID: {0} - Expected a rank of ACE, got {o_TestCard.getRank()} instead"

def test_ace_of_diamonds():
    id = 0 + 39
    o_TestCard = Card(id)
    assert o_TestCard.getSuit() == 3, f"ID: {id} - Expected a Suit of 3, got {o_TestCard.getSuit()} instead"
    assert o_TestCard.getSuitLiteral() == "DIAMOND", f"ID: {id} - Expected a Suit of DIAMOND, got {o_TestCard.getSuitLiteral()} instead"
    assert o_TestCard.getRank()  == 0, f"ID: {0} - Expected a rank of 0, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "ACE", f"ID: {0} - Expected a rank of ACE, got {o_TestCard.getRank()} instead"

def test_king_of_spades():
    id = 12
    o_TestCard = Card(id)
    assert o_TestCard.getSuit() == 0, f"ID: {id} - Expected a Suit of 0, got {o_TestCard.getSuit()} instead"
    assert o_TestCard.getSuitLiteral() == "SPADE", f"ID: {id} - Expected a Suit of SPADE, got {o_TestCard.getSuitLiteral()} instead"
    assert o_TestCard.getRank()  == 12, f"ID: {0} - Expected a rank of 12, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "KING", f"ID: {0} - Expected a rank of KING, got {o_TestCard.getRank()} instead"

def test_ace_of_clubs():
    id = 12 + 13
    o_TestCard = Card(id)
    assert o_TestCard.getSuit() == 1, f"ID: {id} - Expected a Suit of 1, got {o_TestCard.getSuit()} instead"
    assert o_TestCard.getSuitLiteral() == "CLUB", f"ID: {id} - Expected a Suit of CLUB, got {o_TestCard.getSuitLiteral()} instead"
    assert o_TestCard.getRank()  == 12, f"ID: {0} - Expected a rank of 12, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "KING", f"ID: {0} - Expected a rank of KING, got {o_TestCard.getRank()} instead"

def test_ace_of_hearts():
    id = 12 + 26
    o_TestCard = Card(id)
    assert o_TestCard.getSuit() == 2, f"ID: {id} - Expected a Suit of 2, got {o_TestCard.getSuit()} instead"
    assert o_TestCard.getSuitLiteral() == "HEART", f"ID: {id} - Expected a Suit of HEART, got {o_TestCard.getSuitLiteral()} instead"
    assert o_TestCard.getRank()  == 12, f"ID: {0} - Expected a rank of 12, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "KING", f"ID: {0} - Expected a rank of KING, got {o_TestCard.getRank()} instead"

def test_ace_of_diamonds():
    id = 12 + 39
    o_TestCard = Card(id)
    assert o_TestCard.getSuit() == 3, f"ID: {id} - Expected a Suit of 3, got {o_TestCard.getSuit()} instead"
    assert o_TestCard.getSuitLiteral() == "DIAMOND", f"ID: {id} - Expected a Suit of DIAMOND, got {o_TestCard.getSuitLiteral()} instead"
    assert o_TestCard.getRank()  == 12, f"ID: {0} - Expected a rank of 12, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "KING", f"ID: {0} - Expected a rank of KING, got {o_TestCard.getRank()} instead"

def test_deck_creation():
    o_TestDeck = Deck()
    for i in range(0, 52):
        assert str(o_TestDeck.a_Cards[i]) == str(Card(i)), f"Expected {o_TestDeck.a_Cards[i]}, got {Card(i)}"

def test_shuffle():
    o_TestDeck1 = Deck()
    o_TestDeck2 = Deck()
    o_TestDeck1.shuffle()
    o_TestDeck2.shuffle()
    assert (o_TestDeck1.a_CardsById != o_TestDeck2.a_CardsById)

def test_draw_unshuffled():
    o_TestDeck = Deck()
    o_TestCard = Card(0)
    assert str(o_TestDeck.drawCard()) == str(o_TestCard)
    assert str(o_TestDeck.a_DrawnCards[0]) == str(o_TestCard)
    assert len(o_TestDeck.a_DrawnCards) == 1
    assert len(o_TestDeck.a_Cards)      == 51
    assert len(o_TestDeck.a_CardsById)  == 51
    assert len(o_TestDeck.a_DrawnCardsById) == 1
    assert o_TestCard.i_ID not in o_TestDeck.a_CardsById 
    assert o_TestCard.i_ID in o_TestDeck.a_DrawnCardsById

def test_multi_draw():
    for i in range(0, 52):
        o_TestDeck = Deck()
        o_TestDeck.shuffle()
        o_DrawnCards = o_TestDeck.drawCards(i)
        for o_Card in o_DrawnCards:
            assert o_Card.i_ID not in o_TestDeck.a_CardsById
            assert o_Card.i_ID in o_TestDeck.a_DrawnCardsById
            assert len(o_TestDeck.a_DrawnCards) == i
            assert len(o_TestDeck.a_DrawnCardsById) == i
            assert len(o_TestDeck.a_Cards)      == 52 - i
            assert len(o_TestDeck.a_CardsById)  == 52 - i
