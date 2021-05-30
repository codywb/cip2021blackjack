import random

"""
Filename: blackjack.py
This program simulates a game of blackjack between an AI dealer and a single human player.
"""

# this designates colors for printing to the terminal
class bcolors:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

HIDDEN = '🂠' # For representing the dealer's face-down card


# These 4 dictionaries represent all the cards in the deck by suit.
SPADES = {
    'A': {'Name': 'Ace of Spades', 'Value': 11, 'Icon': ['🂡', '(A♠)']},
    '2': {'Name': 'Two of Spades','Value': 2, 'Icon': ['🂢', '(2♠)']},
    '3': {'Name': 'Three of Spades', 'Value': 3, 'Icon': ['🂣', '(3♠)']},
    '4': {'Name': 'Four of Spades', 'Value': 4, 'Icon': ['🂤', '(4♠)']},
    '5': {'Name': 'Five of Spades', 'Value': 5, 'Icon': ['🂥', '(5♠)']},
    '6': {'Name': 'Six of Spades', 'Value': 6, 'Icon': ['🂦', '(6♠)']},
    '7': {'Name': 'Seven of Spades', 'Value': 7, 'Icon': ['🂧', '(7♠)']},
    '8': {'Name': 'Eight of Spades', 'Value': 8, 'Icon': ['🂨', '(8♠)']},
    '9': {'Name': 'Nine of Spades', 'Value': 9, 'Icon': ['🂩', '(9♠)']},
    '10': {'Name': 'Ten of Spades', 'Value': 10, 'Icon': ['🂪', '(10♠)']},
    'J': {'Name': 'Jack of Spades', 'Value': 10, 'Icon': ['🂫', '(J♠)']},
    'Q': {'Name': 'Queen of Spades', 'Value': 10, 'Icon': ['🂭', '(Q♠)']},
    'K': {'Name': 'King of Spades', 'Value': 10, 'Icon': ['🂮', '(K♠)']}
}

HEARTS = {
    'A': {'Name': 'Ace of Hearts', 'Value': 11, 'Icon': ['🂱', '(A♥)']},
    '2': {'Name': 'Two of Hearts','Value': 2, 'Icon': ['🂲', '(2♥)']},
    '3': {'Name': 'Three of Hearts', 'Value': 3, 'Icon': ['🂳', '(3♥)']},
    '4': {'Name': 'Four of Hearts', 'Value': 4, 'Icon': ['🂴', '(4♥)']},
    '5': {'Name': 'Five of Hearts', 'Value': 5, 'Icon': ['🂵', '(5♥)']},
    '6': {'Name': 'Six of Hearts', 'Value': 6, 'Icon': ['🂶', '(6♥)']},
    '7': {'Name': 'Seven of Hearts', 'Value': 7, 'Icon': ['🂷', '(7♥)']},
    '8': {'Name': 'Eight of Hearts', 'Value': 8, 'Icon': ['🂸', '(8♥)']},
    '9': {'Name': 'Nine of Hearts', 'Value': 9, 'Icon': ['🂹', '(9♥)']},
    '10': {'Name': 'Ten of Hearts', 'Value': 10, 'Icon': ['🂺', '(10♥)']},
    'J': {'Name': 'Jack of Hearts', 'Value': 10, 'Icon': ['🂻', '(J♥)']},
    'Q': {'Name': 'Queen of Hearts', 'Value': 10, 'Icon': ['🂽', '(Q♥)']},
    'K': {'Name': 'King of Hearts', 'Value': 10, 'Icon': ['🂾', '(K♥)']}
}

DIAMONDS = {
    'A': {'Name': 'Ace of Diamonds', 'Value': 11, 'Icon': ['🃁', '(A♦)']},
    '2': {'Name': 'Two of Diamonds','Value': 2, 'Icon': ['🃂', '(2♦)']},
    '3': {'Name': 'Three of Diamonds', 'Value': 3, 'Icon': ['🃃', '(3♦)']},
    '4': {'Name': 'Four of Diamonds', 'Value': 4, 'Icon': ['🃄', '(4♦)']},
    '5': {'Name': 'Five of Diamonds', 'Value': 5, 'Icon': ['🃅', '(5♦)']},
    '6': {'Name': 'Six of Diamonds', 'Value': 6, 'Icon': ['🃆', '(6♦)']},
    '7': {'Name': 'Seven of Diamonds', 'Value': 7, 'Icon': ['🃇', '(7♦)']},
    '8': {'Name': 'Eight of Diamonds', 'Value': 8, 'Icon': ['🃈', '(8♦)']},
    '9': {'Name': 'Nine of Diamonds', 'Value': 9, 'Icon': ['🃉', '(9♦)']},
    '10': {'Name': 'Ten of Diamonds', 'Value': 10, 'Icon': ['🃊', '(10♦)']},
    'J': {'Name': 'Jack of Diamonds', 'Value': 10, 'Icon': ['🃋', '(J♦)']},
    'Q': {'Name': 'Queen of Diamonds', 'Value': 10, 'Icon': ['🃍', '(Q♦)']},
    'K': {'Name': 'King of Diamonds', 'Value': 10, 'Icon': ['🃎', '(K♦)']}
}

CLUBS = {
    'A': {'Name': 'Ace of Clubs', 'Value': 11, 'Icon': ['🃑', '(A♣)']},
    '2': {'Name': 'Two of Clubs','Value': 2, 'Icon': ['🃒', '(2♣)']},
    '3': {'Name': 'Three of Clubs', 'Value': 3, 'Icon': ['🃓', '(3♣)']},
    '4': {'Name': 'Four of Clubs', 'Value': 4, 'Icon': ['🃔', '(4♣)']},
    '5': {'Name': 'Five of Clubs', 'Value': 5, 'Icon': ['🃕', '(5♣)']},
    '6': {'Name': 'Six of Clubs', 'Value': 6, 'Icon': ['🃖', '(6♣)']},
    '7': {'Name': 'Seven of Clubs', 'Value': 7, 'Icon': ['🃗', '(7♣)']},
    '8': {'Name': 'Eight of Clubs', 'Value': 8, 'Icon': ['🃘', '(8♣)']},
    '9': {'Name': 'Nine of Clubs', 'Value': 9, 'Icon': ['🃙', '(9♣)']},
    '10': {'Name': 'Ten of Clubs', 'Value': 10, 'Icon': ['🃚', '(10♣)']},
    'J': {'Name': 'Jack of Clubs', 'Value': 10, 'Icon': ['🃛', '(J♣)']},
    'Q': {'Name': 'Queen of Clubs', 'Value': 10, 'Icon': ['🃝', '(Q♣)']},
    'K': {'Name': 'King of Clubs', 'Value': 10, 'Icon': ['🃞', '(K♣)']}
}

# This line builds a deck represented by a list using the 4 dictionaries for each suit.
DECK = [SPADES, HEARTS, CLUBS, DIAMONDS]

# Set the value of the player's starting purse available for betting.
INIT_PURSE = 500

def main():
    deck = DECK # initialize deck for game
    purse = INIT_PURSE # set initial purse amount
    num_cards = get_remaining_cards(deck)
    show_greeting()

    while purse > 0:
        print(f"\nThere are {num_cards} cards remaining in the deck.")
        player_bet = get_wager(purse)
        print("Dealing starting hands...")
        try:
            player_hand = deal_new_hand(deck)
            dealer_hand = deal_new_hand(deck)
            show_current_hands(player_hand, dealer_hand)
            player_score = calculate_score(player_hand)
            dealer_score = calculate_score(dealer_hand)
            player_turn_score = player_phase(player_hand, dealer_hand, player_score, deck)
            dealer_turn_score = dealer_phase(dealer_hand, dealer_score, deck)
        except IndexError:
            print("The deck has run out of cards. Game over!")
            break
        turn_result = conclude_turn(player_turn_score, dealer_turn_score, player_bet, purse)
        purse = turn_result
        if purse < 1:
            print("You have run out of money. Game over!")
            break
        num_cards = get_remaining_cards(deck)




def conclude_turn(player_score, dealer_score, player_bet, purse):
    """
    Takes in the current scores, bet, and purse amoutnts and calculates
    what the new purse value will be.
    :param player_score: current value of player's hand
    :param dealer_score: current valye of dealer's hand
    :param player_bet: how much the player bet at the start
    :param purse: current value of purse at start of turn
    :return: the new value of the purse
    """
    print(f"\nPlayer score: {player_score} \tDealer score: {dealer_score}")
    if player_score > 21:
        print("You busted. The dealer wins!")
        purse -= player_bet
        return purse
    if dealer_score > 21 and player_score <= 21:
        print("The dealer busted. You win!")
        purse += player_bet
        return purse
    if player_score > dealer_score:
        print("You win!")
        purse += player_bet
        return purse
    if player_score == dealer_score:
        print("It's a draw! Dealer wins draws.")
        purse -= player_bet
        return purse
    if player_score < dealer_score:
        print("You lose!")
        purse -= player_bet
        return purse


def player_phase(player_hand, dealer_hand, player_score, deck):
    """
    Prompts player to choose whether they would like to hit or stand.
    If 'hit', a card is added to hand and the score is re-calculated.
    If 'stand', the current score is returned to main().
    :param player_hand: current cards in the player's hand
    :param dealer_hand: current cards in dealer's hand
    :param player_score: current value of cards in player's hand
    :param deck: current value of deck
    :return: the updated value of the cards in player's hand
    """
    while True:
        player_choice = get_player_choice(player_score)
        if player_choice == 'hit':
            new_card = select_card(deck)
            player_hand.append(new_card)
            show_current_hands(player_hand, dealer_hand)
            player_score = calculate_score(player_hand)
            if player_score > 21:
                return player_score
        elif player_choice == 'stay':
            return player_score


def dealer_phase(dealer_hand, dealer_score, deck):
    """
    Simple function for executing the dealer's phase of the turn.
    If 'hit', a card is added to hand and the score is re-calculated.
    If 'stand', the current score is returned to main().
    :param dealer_hand: current cards in dealer's hand
    :param dealer_score: current value of card sin dealer's hand
    :param deck: current value of deck
    :return: the updated value of the cards in dealer's hand
    """
    while True:
        dealer_choice = get_dealer_choice(dealer_score)
        if dealer_choice == 'hit':
            new_card = select_card(deck)
            dealer_hand.append(new_card)
            dealer_score = calculate_score(dealer_hand)
            if dealer_score > 21:
                return dealer_score
        elif dealer_choice == 'stay':
            return dealer_score


def get_dealer_choice(score):
    """
    Simple function for getting the dealer's choice.
    The dealer will hit on anything under 17 and stay otherwise.
    :param score: current value of cards in hand
    :return: either 'hit' or 'stay'
    """
    if score < 17:
        return 'hit'
    return 'stay'


def get_player_choice(score):
    """
    Simple function for getting the player's choice.
    Prompts player to enter 'h' or 's' to hit or stand.
    :param score: current value of cards in hand
    :return: either 'hit' or 'stay'
    """
    while True:
        print(f"The value of your hand is currently {score}.")
        choice = input("Would you like to [H]it or [S]tand? ")
        if choice in ['H', 'h']:
            return 'hit'
        elif choice in ['S', 's']:
            return 'stay'
        else:
            print(f"\n{bcolors.RED}Please enter an 'H' to hit or 'S' to stand.{bcolors.ENDC}\n")


def calculate_score(hand):
    """
    Calculates the value of the total cards in a hand.
    If there is an ace present, this function correctly adjusts the total value
    of the hand so as to prevent an unexpected bust.
    :param hand: current cards in hand
    :return: the total value of the cards in hand
    """
    total = 0
    num_aces = 0
    for i in range(len(hand)):
        if 'A' in hand[i]:
            num_aces += 1 # checks for presence and number of Aces
    if num_aces > 0:
        for card in hand:
            total += card[1]['Value']
        if total > 21:
            total -= 10 * (num_aces-1) # reduces value of Ace to 1 from default value of 11 if necessary
    else:
        for card in hand:
            total += card[1]['Value']
    return total


def get_remaining_cards(deck):
    """
    Simple function for checking the total number of cards remaining
    in the deck.
    :param deck: current value of the deck
    :return: the number of cards in the deck
    """
    #num_cards = len(deck[0]) + len(deck[1]) + len(deck[2]) + len(deck[3])
    num_cards = 0
    for suit in deck:
        num_cards += len(suit)
    return num_cards


def show_greeting():
    """
    Prints a simple greeting to the player at the start of the game.
    :return: none
    """
    print(f"♠ {bcolors.RED}♥{bcolors.ENDC} {bcolors.BOLD}{bcolors.UNDERLINE}Code in Place 2021 - "
          f"Blackjack{bcolors.ENDC} {bcolors.RED}♦{bcolors.ENDC} ♣")
    print()
    print(f"Welcome to the table!")
    print()


def get_wager(purse):
    """
    Prompts the user for a bet between $1-100, checks to ensure it is valid, and returns it to main().
    If invalid, re-prompts until valid input received.
    :param purse: the current value of the player's purse available for betting
    :return: an int between 1-100
    """
    while True:
        try:
            print(f"You currently have {bcolors.GREEN}${purse}{bcolors.ENDC}.")
            wager = int(input("Please place your bet ($1-100): "))
            if wager_is_valid(wager, purse):
                return wager
        except ValueError:
            print(f"{bcolors.RED}Invalid input. Please enter a number between 1 and 100.{bcolors.ENDC}")


def show_current_hands(player_hand, dealer_hand):
    """
    Displays the cards currently in the dealer's and player's hands with icons.
    :param player_hand: current cards in player's hand
    :param dealer_hand: current cards in dealer's hands
    :return: none
    """
    print("\nThe dealer is showing:")
    print(f"{dealer_hand[0][1]['Icon'][0]} {dealer_hand[0][1]['Name']} {dealer_hand[0][1]['Icon'][1]}")
    print(f"{HIDDEN} Unknown Card")
    print("")
    print("Your current hand:")
    for card in player_hand:
        print(f"{card[1]['Icon'][0]} {card[1]['Name']} {card[1]['Icon'][1]}")
    print("")


def deal_new_hand(deck):
    """
    Deals a starting hand of 2 randomly selected cards.
    :param deck: current value of deck
    :return: a list with 2 cards
    """
    cards = []
    card1 = select_card(deck)
    card2 = select_card(deck)
    cards.append(card1)
    cards.append(card2)
    return cards


def select_card(deck):
    """
    Randomly selects one of four dictionaries in the deck list representing suits,
    then randomly selects one card from that suit. If there are no more cards of that
    suit, the dictionary of that suit is deleted from the deck and a new selection is
    made.
    :param deck: current value of deck
    :return: a tuple representing the chosen card
    """
    while True:
        suit = random.choice(deck)
        if not suit:
            index = deck.index(suit)
            deck.pop(index)
        else:
            card = random.choice(list(suit.items()))
            suit.pop(card[0])
            break
    return card


def wager_is_valid(wager, purse):
    """
    Checks to make sure the value of 'wager' is between 1 and 100 and less than the current value of 'purse' in main().
    :param wager: amount of desired bet entered by user
    :param purse: current value of player's purse available to bet
    :return: True or False depending on whether the user's input passed as 'wager' is valid or not
    """
    if 1 <= wager <= 100 and purse >= wager:
        return True
    elif wager >= purse:
        print(f"{bcolors.RED}Sorry, you can't bet more money than you currently have!{bcolors.ENDC}")
        return False
    else:
        print(f"{bcolors.RED}Invalid input. Please enter a number between 1 and 100.{bcolors.ENDC}")
        return False


if __name__ == "__main__":
    main()
