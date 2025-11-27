import random
import os
import time

CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
SUITS = ['♠', '♥', '♦', '♣']
NAMES = {11: 'A', 10: '10', 9: '9', 8: '8', 7: '7', 6: '6', 5: '5', 4: '4', 3: '3', 2: '2'}

def wait():
    for dot in "....": 
        print(dot, end="", flush=True)
        time.sleep(0.5)
    print()

def deal_card():
    return random.choice(list(NAMES.keys())), random.choice(SUITS)

def calculate_score(hand):
    values = [card[0] for card in hand]
    score = sum(values)
    while score > 21 and 11 in values:
        values[values.index(11)] = 1
        score = sum(values)
    return score

def draw_cards(hand, hide_first=False):
    top, mid, bot = "", "", ""
    for i, (val, suit) in enumerate(hand):
        if hide_first and i == 0:
            top += "┌─────┐ "
            mid += "│  ?  │ "
            bot += "└─────┘ "
        else:
            symbol = NAMES[val]
            top += "┌─────┐ "
            mid += f"│{symbol:<2}{suit:>2} │ "
            bot += "└─────┘ "
    return f"{top}\n{mid}\n{bot}"

def print_hands(player, dealer, hide_dealer=True):
    os.system('cls')
    print("=== Blackjack ===\n")
    print("Dealer:")
    print(draw_cards(dealer, hide_first=hide_dealer))
    print("\nJucator:")
    print(draw_cards(player))
    print(f"Scor: {calculate_score(player)}")

def blackjack():
    player = [deal_card(), deal_card()]
    dealer = [deal_card(), deal_card()]

    while True:
        os.system('cls')
        print_hands(player, dealer, hide_dealer=True)
        player_score = calculate_score(player)
        if player_score >= 21:
            break

        choice = input("\n[h] sau [s]: ").lower()
        if choice == 'h':
            player.append(deal_card())
        elif choice == 's':
            break

    while calculate_score(dealer) < 17:
        os.system('cls')
        dealer.append(deal_card())
        print_hands(player, dealer, hide_dealer=True)
        for i in range(4):
            print(".", end="", flush=True)
            time.sleep(0.5)

    print_hands(player, dealer, hide_dealer=False)
    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    print("\nRezultat", end="")
    wait()

    if player_score > 21:
        print("Ai pierdut.")
    elif dealer_score > 21 or player_score > dealer_score:
        print("Ai castigat.")
    elif player_score < dealer_score:
        print("Dealerul a castigat.")
    else:
        print("Egalitate.")

    print()
    wait()
    input("Apasa Enter...")

def menu():
    while True:
        os.system('cls')
        print("=== Meniu Blackjack ===")
        print("1. Joc nou")
        print("2. Iesire")
        choice = input("> ")
        if choice == "1":
            blackjack()
        elif choice == "2":
            print("Iesire", end="")
            wait()
            break

menu()
