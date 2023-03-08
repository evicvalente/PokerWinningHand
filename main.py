from deck import Deck
from poker_hand import PokerHand


def simulate():
    """
    Simulation of the game
    :return:
    """
    score = 0
    deck = Deck()
    deck.shuffle()
    hand1 = PokerHand([])
    hand2 = PokerHand([])
    while len(deck.cards) >= 10:
        hand1.clear()
        hand2.clear()
        for _ in range(5):
            hand1.add_card(deck.deal())
            hand2.add_card(deck.deal())

        print(f'Hand 1: {hand1}')
        print(f'Hand 2: {hand2}')
        n = input("Enter the Hand Number which is worth more [Enter 0 if equal]: ")
        while n not in ['1', '2', '0']:
            n = input("Enter the Hand Number which is worth more [Enter 0 if equal]: ")
        n = int(n)
        cmp = hand1.compare_to(hand2)
        if (cmp < 0 and n != 2) or (cmp > 0 and n != 1) or (cmp == 0 and n != 0):
            break
        print("Good job!")
        score += 1

    print(f"GAME OVER! Your Score: {score}")


def test_compare_to():
    """
    Tests the compare_to method
    :return:
    """
    print("Testing compare_to method")

    # Test Case 1: Hands with different high card
    hand_a = PokerHand([Card("S", 9), Card("D", 5), Card("C", 8), Card("H", 6), Card("S", 4)])
    hand_b = PokerHand([Card("D", 10), Card("H", 7), Card("C", 9), Card("S", 5), Card("H", 4)])
    result = hand_a.compare_to(hand_b)
    if result < 0:
        print("Test Case 1: PASS")
    else:
        print("Test Case 1: FAIL")

    # Test Case 2: Hands with same high card
    hand_a = PokerHand([Card("S", 9), Card("D", 9), Card("C", 8), Card("H", 6), Card("S", 4)])
    hand_b = PokerHand([Card("D", 9), Card("H", 9), Card("C", 8), Card("S", 5), Card("H", 4)])
    result = hand_a.compare_to(hand_b)
    if result == 0:
        print("Test Case 2: PASS")
    else:
        print("Test Case 2: FAIL")

    # Test Case 3: Hands with different pairs
    hand_a = PokerHand([Card("S", 9), Card("D", 9), Card("C", 8), Card("H", 6), Card("S", 4)])
    hand_b = PokerHand([Card("D", 10), Card("H", 10), Card("C", 8), Card("S", 5), Card("H", 4)])
    result = hand_a.compare_to(hand_b)
    if result < 0:
        print("Test Case 3: PASS")
    else:
        print("Test Case 3: FAIL")

    # Test Case 4: Hands with different two pairs
    hand_a = PokerHand([Card("S", 9), Card("D", 9), Card("C", 8), Card("H", 8), Card("S", 4)])
    hand_b = PokerHand([Card("D", 11), Card("H", 11), Card("C", 10), Card("S", 10), Card("H", 4)])
    result = hand_a.compare_to(hand_b)
    if result < 0:
        print("Test Case 4: PASS")
    else:
        print("Test Case 4: FAIL")

    # Test Case 5: Hands with different flushes
    hand_a = PokerHand([Card("S", 9), Card("S", 8), Card("S", 7), Card("S", 6), Card("S", 4)])
    hand_b = PokerHand([Card("H", 9), Card("H", 8), Card("H", 7), Card("H", 6), Card("H", 4)])
    result = hand_a.compare_to(hand_b)
    if result < 0:
        print("Test Case 5: PASS")
    else:
        print("Test Case 5: FAIL")

if __name__ == '__main__':
    simulate()
