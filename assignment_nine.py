import card
import deck

def deal_cards(a_deck):
    c = []
    for x in range(5):
        n = a_deck.deal()
        c.append(n)
    return c


def compare_cards(card1,card2):
    if card1 > card2 :
        return "Player One"
    if card2 > card1 :
        return "Player Two"
def main():
    k = deck.Deck()
    k.shuffle()
    player_one= []
    player_one += deal_cards(k)
    player_two = []
    player_two += deal_cards(k)
    a = player_two(0)
    b = player_two(1)
    c = player_two(2)
    d = player_two(3)
    e = player_two(4)
    f = player_one(0)
    g = player_one(1)
    h = player_one(2)
    i = player_one(3)
    j = player_one(4)
    compare_cards(a,f)
    compare_cards(b,g)
    compare_cards(c,h)
    compare_cards(d,i)
    compare_cards(e,j)

main()



