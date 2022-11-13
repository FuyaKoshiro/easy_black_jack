import random
from art import win, lose, logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

hit = True
draw = True
user_cards = []
dealer_cards = []
user_sum = 0
dealer_sum = 0

def add(player_list):
    player_list.append(random.choice(cards))
    return player_list

def sum_cards(player_list, player_sum):
    for i in player_list:
        player_sum += i
    return player_sum

def user_play(user_sum):
    if user_sum > 21:
        print("you lose")
        print(lose)
        hit = False
    elif user_sum == 21:
        hit = False
    elif user_sum < 21:
        play = input("hit or stand: ")
        if play == "hit":
            hit = True
        elif play == "stand":
            hit = False
        else:
            print("typed wrong")
    return hit

def dealer_play(dealer_sum, user_sum):
    if dealer_sum > 21:
        print("you won")
        print(win)
        draw = False
    elif 16 < dealer_sum <= 21:
        draw = False
        comparison(user_sum, dealer_sum)
    else:
        draw = True
        input("press enter")
    return draw

def comparison(user_sum, dealer_sum):
    if user_sum > dealer_sum:
        print("you won")
        print(win)
    elif user_sum == dealer_sum:
        print("draw")
    else:
        print("you lost")
        print(lose)

def first_turn(user_cards, dealer_cards):
    for i in range(0, 2):
        add(user_cards)
        add(dealer_cards)
    
    print(f"You : {user_cards} \nDealer : [{dealer_cards[0]}, ??]")
    return user_cards, dealer_cards

#-----------------------from here-------------
print(logo)
first_turn(user_cards, dealer_cards)

while hit:
    user_sum = 0
    user_sum = sum_cards(user_cards, user_sum)
    print(f"total of your cards is {user_sum}")
    hit = user_play(user_sum)
    if hit == True:
        user_cards = add(user_cards)
        print("You added a card")
        print(f"You : {user_cards}")

if user_sum > 21:
    print("finished")
else:
    input("dealer's turn. press enter to go on")

    while draw:
        print(f"Dealer : {dealer_cards}")
        dealer_sum = 0
        dealer_sum = sum_cards(dealer_cards, dealer_sum)
        print(f"total of dealer's cards is {dealer_sum}")
        draw = dealer_play(dealer_sum, user_sum)
        if draw == True:
            dealer_cards = add(dealer_cards)
            print("Dealer added a card")
    print("finished")