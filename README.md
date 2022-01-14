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
- Providing a blank `i_ID` produces a random card

#### Class methods
##### `Card.getRank()`
Returns the rank of the created card, an integer value in the range [0, 12] (inclusive)

##### `Card.getRankLiteral()`
Returns the literal string of the created card, example: `"TWO"`, `"KING"`, `"ACE"`

##### `Card.getSuit()`
Returns the integer representation of the created card's suit, represented as follows:
- If the card is a spade, `.getSuit()` returns `0`
- If the card is a club, `.getSuit()` returns `1`
- If the card is a heart, `.getSuit()` returns `2`
- If the card is a diamond, `.getSuit()` returns `3`

##### `Card.getSuitLiteral()`
Returns the literal representation of the created card's suit, represented as follows:
- If the card is a spade, `.getSuit()` returns `"SPADE"`
- If the card is a club, `.getSuit()` returns `"CLUB"`
- If the card is a heart, `.getSuit()` returns `"HEART"`
- If the card is a diamond, `.getSuit()` returns `"DIAMOND"`

### `Deck` class

#### Declaration
The class must first be imported with:
```
from python-card-models import Deck
```

Once imported, a Deck object can be created with:
```
o_DeckObjectName = Card()
```

#### Class attributes
##### `Deck.a_Cards`
Contains the Card objects that remain undrawn in the deck. This is initially set as an array of 52 cards, in order from Ace to King, in the order of spades, clubs, hearts and diamonds.

##### `Deck.a_DrawnCards`
Contains the Card objects that have been drawn from the deck. This is initially set to empty. It should be noted that the intersection of the `Deck.a_Cards` and `Deck.a_DrawnCards` is 0, as a card cannot be undrawn and drawn at the same time.

##### `Deck.a_CardsById`
Contains the integer Card IDs that remain undrawn in the deck. This is initially set as an array of integers in order from 0 to 51

##### `Deck.a_DrawnCardsById`
Contains the integer Card IDs that have been drawn from the deck. This is initially set to empty. It should be noted that the intersection of the `Deck.a_CardsById` and `Deck.a_DrawnCardsById` is 0, as a card cannot be undrawn and drawn at the same time.

#### Class methods
##### `Deck.shuffle()`
Shuffles the deck randomly, scrambling the order of both `Deck.a_CardsById` and `Deck.a_Cards`. Note that shuffling does not affect the drawn card arrays.

##### `Deck.reset()`
Resets the deck, unshuffling the cards and moving all drawn cards back to the undrawn array.

##### `Deck.drawCard()`
Draws and returns a card from the `Deck.a_Cards`, moving it into `Deck.a_DrawnCards`, it also moves the card's ID from `Deck.a_CardsByID` into `Deck.a_CardsById`. Cards are drawn from the first index of `Deck.a_Cards`, for example, drawing a card from an unshuffling deck will always return the ace of spades.

##### `Deck.drawCards(i_NumCards)`
Draws and returns an array of length `i_NumCards`, containing `Card` objects from the first indexes of `Deck.a_Cards`. This means that drawing 5 cards from an unshuffled deck will return the ace, two, three, four and five of spades.



