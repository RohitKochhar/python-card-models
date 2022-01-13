# python-card-models
Python classes to simulate playing cards

## Usage

### `Card` class

#### Declaration
The class must first be imported with:
```
from python-card-models import Card
```

Once imported, a card object can be created with:
```
o_CardObjectName = Card(i_ID)
```

`i_ID` is an integer value between 0 and 51, corresponding to a unique card in the deck. For example:
- `i_ID` in the range [0, 12] (inclusive) corresponds to an spade, with rank i_ID (jack, queen, king an ace  have i_ID 10, 11, 12 and 0)
- `i_ID` in the range [13, 25] (inclusive) corresponds to a club, with rank i_ID - 13
- `i_ID` in the range [26, 38] (inclusive) corresponds to a heart, with rank i_ID - 26
- `i_ID` in the range [39, 51] (inclusive) corresponds to a diamond, with rank i_ID - 39
- Providing a blank i_ID produces a random card

#### Class methods
##### `Card.getRank()`
Returns the rank of the created card, an integer value in the range [0, 12] (inclusive)

##### `Card.getRankLiteral()`
Returns the literal string of the created card, example: "TWO", "KING", "ACE"

##### `Card.getSuit()`
Returns the integer representation of the created card's suit, represented as follows:
- If the card is a spade, `.getSuit()` returns a 0
- If the card is a club, `.getSuit()` returns a 1
- If the card is a heart, `.getSuit()` returns a 2
- If the card is a diamond, `.getSuit()` returns a 3

##### `Card.getSuitLiteral()`
Returns the literal representation of the created card's suit, represented as follows:
- If the card is a spade, `.getSuit()` returns "SPADE"
- If the card is a club, `.getSuit()` returns "CLUB"
- If the card is a heart, `.getSuit()` returns "HEART"
- If the card is a diamond, `.getSuit()` returns "DIAMOND"

