import random

def bets(chips ,bet ,player_money): 
    print(f"You have ${player_money} to bet.")
    print("Available chips: ", chips[1:])
    while True:    
        choice = int(input("Place your bets: "))
        if choice in chips and choice <= player_money and bet <= player_money:
            bet += choice
            c = input(f"Do you want to add another chip? You have ${player_money-bet} left to bet. (y/n): ")
            if c == 'n':
                print(f"You have bet ${bet}.")
                break
        else:
            print("Invalid bet. Please choose a valid chip.")
    return bet, player_money

def deal_card(person, cards):
    card = random.choice(list(cards.keys()))
    person.append(card)
    return person

def calculate_score(hand, cards):
    score = sum(cards[card] for card in hand)
    if score > 21 and 'Ace' in hand:
        score -= 10
    return score

def display_hands(player, dealer, cards):
    print(f"Your cards: {player} (Score: {calculate_score(player, cards)})")
    print(f"Dealer's cards: {dealer[0]} and a hidden card")

def hit_or_stand(player, dealer, cards):
    while True:
        choice = input("Do you want to hit or stand? (hit/stand): ")
        if choice == 'hit':
            player = deal_card(player, cards)
            display_hands(player, dealer, cards)
            if calculate_score(player, cards) > 21:
                print("You bust! Dealer wins.")
                return None
            if calculate_score(player, cards) == 21:
                print("You have 21! Let's see what the dealer has.")
                return player
        elif choice == 'stand':
            return player
        else:
            print("Invalid choice. Please enter 'hit' or 'stand'.")

def win_or_lose(player_money, bet,player, dealer, cards):
    if player is not None:
        while calculate_score(dealer, cards) < 17:
            dealer = deal_card(dealer, cards)
        print(f"Dealer's cards: {dealer} (Score: {calculate_score(dealer, cards)})")
        if calculate_score(dealer, cards) > 21:
            print("Dealer busts! You win.")
            player_money += bet
        elif calculate_score(player, cards) > calculate_score(dealer, cards):
            print("You win!")
            player_money += bet
        elif calculate_score(player, cards) < calculate_score(dealer, cards):
            print("Dealer wins!")
            player_money -= bet
        else:
            print("It's a tie!")
        return player_money
    else:
        player_money -= bet
        return player_money

def play_game(player_money):
    cards = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
    chips = [0, 1, 10, 100, 500]
    bet = 0
    player = []
    dealer = []
    print("Welcome to Blackjack!")
    bet, player_money = bets(chips, bet, player_money)
    player = deal_card(player, cards)
    player = deal_card(player, cards)
    dealer = deal_card(dealer, cards)
    dealer = deal_card(dealer, cards)
    display_hands(player, dealer, cards)
    player = hit_or_stand(player, dealer, cards)
    player_money = win_or_lose(player_money, bet,player, dealer, cards)
    choice = input("Do you want to play again? (y/n): ")
    if choice == 'y':
        play_game(player_money)
    else:
        print("Thanks for playing! Goodbye.")

play_game(5000)

