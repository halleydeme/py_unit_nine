import card
import deck


# new_card = card.Card(9, "Hearts")
# print(new_card.rank)
# other_card = card.Cards(5, "Clubs")
# print(other_card.rank)

new_deck = deck.Deck()
print (new_deck.cards[4].rank + " of " + new_deck.cards[4].suit)


