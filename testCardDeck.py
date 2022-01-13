from CardDeck import Card, Deck

def test_spade_assignment():
    for i in range(0, 12):
        o_TestCard  = Card(i)
        assert o_TestCard.getSuite() == 0, f"ID: {i} - Expected a suite of 0, got {o_TestCard.getSuite()} instead"
        assert o_TestCard.getSuiteLiteral() == "SPADE", f"ID: {i} - Expected a suite of SPADE, got {o_TestCard.getSuiteLiteral()} instead"

def test_club_assignment():
    for i in range(13, 25):
        o_TestCard  = Card(i)
        assert o_TestCard.getSuite() == 1, f"ID: {i} - Expected a suite of 1, got {o_TestCard.getSuite()} instead"
        assert o_TestCard.getSuiteLiteral() == "CLUB", f"ID: {i} - Expected a suite of CLUB, got {o_TestCard.getSuiteLiteral()} instead"

def test_heart_assignment():
    for i in range(26, 38):
        o_TestCard  = Card(i)
        assert o_TestCard.getSuite() == 2, f"ID: {i} - Expected a suite of 2, got {o_TestCard.getSuite()} instead"
        assert o_TestCard.getSuiteLiteral() == "HEART", f"ID: {i} - Expected a suite of HEART, got {o_TestCard.getSuiteLiteral()} instead"


def test_diamond_assignment():
    for i in range(39, 52):
        o_TestCard  = Card(i)
        assert o_TestCard.getSuite() == 3, f"ID: {i} - Expected a suite of 3, got {o_TestCard.getSuite()} instead"
        assert o_TestCard.getSuiteLiteral() == "DIAMOND", f"ID: {i} - Expected a suite of DIAMOND, got {o_TestCard.getSuiteLiteral()} instead"

def test_all_card_assignment():
    for i in range(0, 52):
        o_TestCard = Card(i)
        if i <= 12:
            assert o_TestCard.getSuite() == 0, f"ID: {i} - Expected a suite of 0, got {o_TestCard.getSuite()} instead"
            assert o_TestCard.getSuiteLiteral() == "SPADE", f"ID: {i} - Expected a suite of SPADE, got {o_TestCard.getSuiteLiteral()} instead"
            assert o_TestCard.getRank()  == i, f"ID: {i} - Expected a rank of {i}, got {o_TestCard.getRank()} instead"
        if i > 13 and i <= 25:
            assert o_TestCard.getSuite() == 1, f"ID: {i} - Expected a suite of 1, got {o_TestCard.getSuite()} instead"
            assert o_TestCard.getSuiteLiteral() == "CLUB", f"ID: {i} - Expected a suite of CLUB, got {o_TestCard.getSuiteLiteral()} instead"
            assert o_TestCard.getRank()  == i - 13, f"ID: {i} - Expected a rank of {i - 13}, got {o_TestCard.getRank()} instead"        
        if i > 26 and i <= 38:
            assert o_TestCard.getSuite() == 2, f"ID: {i} - Expected a suite of 2, got {o_TestCard.getSuite()} instead"
            assert o_TestCard.getSuiteLiteral() == "HEART", f"ID: {i} - Expected a suite of HEART, got {o_TestCard.getSuiteLiteral()} instead"
            assert o_TestCard.getRank()  == i - 26, f"ID: {i} - Expected a rank of {i - 26}, got {o_TestCard.getRank()} instead"  
        if i > 39 and i <= 51:
            assert o_TestCard.getSuite() == 3, f"ID: {i} - Expected a suite of 3, got {o_TestCard.getSuite()} instead"
            assert o_TestCard.getSuiteLiteral() == "DIAMOND", f"ID: {i} - Expected a suite of DIAMOND, got {o_TestCard.getSuiteLiteral()} instead"
            assert o_TestCard.getRank()  == i - 39, f"ID: {i} - Expected a rank of {i - 39}, got {o_TestCard.getRank()} instead" 

def test_ace_of_spades():
    id = 0
    o_TestCard = Card(id)
    assert o_TestCard.getSuite() == 0, f"ID: {id} - Expected a suite of 0, got {o_TestCard.getSuite()} instead"
    assert o_TestCard.getSuiteLiteral() == "SPADE", f"ID: {id} - Expected a suite of SPADE, got {o_TestCard.getSuiteLiteral()} instead"
    assert o_TestCard.getRank()  == 0, f"ID: {0} - Expected a rank of 0, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "ACE", f"ID: {0} - Expected a rank of ACE, got {o_TestCard.getRank()} instead"

def test_ace_of_clubs():
    id = 0 + 13
    o_TestCard = Card(id)
    assert o_TestCard.getSuite() == 1, f"ID: {id} - Expected a suite of 1, got {o_TestCard.getSuite()} instead"
    assert o_TestCard.getSuiteLiteral() == "CLUB", f"ID: {id} - Expected a suite of CLUB, got {o_TestCard.getSuiteLiteral()} instead"
    assert o_TestCard.getRank()  == 0, f"ID: {0} - Expected a rank of 0, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "ACE", f"ID: {0} - Expected a rank of ACE, got {o_TestCard.getRank()} instead"

def test_ace_of_hearts():
    id = 0 + 26
    o_TestCard = Card(id)
    assert o_TestCard.getSuite() == 2, f"ID: {id} - Expected a suite of 2, got {o_TestCard.getSuite()} instead"
    assert o_TestCard.getSuiteLiteral() == "HEART", f"ID: {id} - Expected a suite of HEART, got {o_TestCard.getSuiteLiteral()} instead"
    assert o_TestCard.getRank()  == 0, f"ID: {0} - Expected a rank of 0, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "ACE", f"ID: {0} - Expected a rank of ACE, got {o_TestCard.getRank()} instead"

def test_ace_of_diamonds():
    id = 0 + 39
    o_TestCard = Card(id)
    assert o_TestCard.getSuite() == 3, f"ID: {id} - Expected a suite of 3, got {o_TestCard.getSuite()} instead"
    assert o_TestCard.getSuiteLiteral() == "DIAMOND", f"ID: {id} - Expected a suite of DIAMOND, got {o_TestCard.getSuiteLiteral()} instead"
    assert o_TestCard.getRank()  == 0, f"ID: {0} - Expected a rank of 0, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "ACE", f"ID: {0} - Expected a rank of ACE, got {o_TestCard.getRank()} instead"

def test_king_of_spades():
    id = 12
    o_TestCard = Card(id)
    assert o_TestCard.getSuite() == 0, f"ID: {id} - Expected a suite of 0, got {o_TestCard.getSuite()} instead"
    assert o_TestCard.getSuiteLiteral() == "SPADE", f"ID: {id} - Expected a suite of SPADE, got {o_TestCard.getSuiteLiteral()} instead"
    assert o_TestCard.getRank()  == 12, f"ID: {0} - Expected a rank of 12, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "KING", f"ID: {0} - Expected a rank of KING, got {o_TestCard.getRank()} instead"

def test_ace_of_clubs():
    id = 12 + 13
    o_TestCard = Card(id)
    assert o_TestCard.getSuite() == 1, f"ID: {id} - Expected a suite of 1, got {o_TestCard.getSuite()} instead"
    assert o_TestCard.getSuiteLiteral() == "CLUB", f"ID: {id} - Expected a suite of CLUB, got {o_TestCard.getSuiteLiteral()} instead"
    assert o_TestCard.getRank()  == 12, f"ID: {0} - Expected a rank of 12, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "KING", f"ID: {0} - Expected a rank of KING, got {o_TestCard.getRank()} instead"

def test_ace_of_hearts():
    id = 12 + 26
    o_TestCard = Card(id)
    assert o_TestCard.getSuite() == 2, f"ID: {id} - Expected a suite of 2, got {o_TestCard.getSuite()} instead"
    assert o_TestCard.getSuiteLiteral() == "HEART", f"ID: {id} - Expected a suite of HEART, got {o_TestCard.getSuiteLiteral()} instead"
    assert o_TestCard.getRank()  == 12, f"ID: {0} - Expected a rank of 12, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "KING", f"ID: {0} - Expected a rank of KING, got {o_TestCard.getRank()} instead"

def test_ace_of_diamonds():
    id = 12 + 39
    o_TestCard = Card(id)
    assert o_TestCard.getSuite() == 3, f"ID: {id} - Expected a suite of 3, got {o_TestCard.getSuite()} instead"
    assert o_TestCard.getSuiteLiteral() == "DIAMOND", f"ID: {id} - Expected a suite of DIAMOND, got {o_TestCard.getSuiteLiteral()} instead"
    assert o_TestCard.getRank()  == 12, f"ID: {0} - Expected a rank of 12, got {o_TestCard.getRank()} instead"
    assert o_TestCard.getRankLiteral()  == "KING", f"ID: {0} - Expected a rank of KING, got {o_TestCard.getRank()} instead"

def test_deck_creation():
    o_TestDeck = Deck()
    for i in range(0, 52):
        assert str(o_TestDeck.a_Cards[i]) == str(Card(i)), f"Expected {o_TestDeck.a_Cards[i]}, got {Card(i)}"