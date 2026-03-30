import random
cards = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
chips = [0, 1, 10, 100, 500]
player_money = 5000
bet = 0
player = []
dealer = []

def bets(chips ,bet ,player_money): 
    print(f"You have ${player_money} to bet.")
    print("Available chips: ", chips[1:])
    while True:    
        choice = int(input("Place your bets: "))
        if choice in chips and choice <= player_money and bet <= player_money:
            bet += choice
            player_money -= choice
            c = input(f"Do you want to add another chip? You have ${player_money} left to bet. (y/n): ")
            if c == 'n':
                print(f"You have bet ${bet}.")
                break
        else:
            print("Invalid bet. Please choose a valid chip.")
    return bet, player_money

def deal_card(person):
    card = random.choice(list(cards.keys()))
    person.append(card)
    return person

bet, player_money = bets(chips, bet, player_money)
player = deal_card(player)
player = deal_card(player)
dealer = deal_card(dealer)
dealer = deal_card(dealer)
print(f"Your cards: {player}")
print(f"Dealer's cards: {dealer[0]} and a hidden card")