"""

Game to play blackjack against the computer

"""

import random
import os
import time

from cards import deck, HIDDEN_CARD, print_cards, BLACKJACK


print(BLACKJACK)
print("Welcome to BlackJack")
starting_amount = int(input("How much '$' would you like to start with: $"))
continue_playing = True
current_amount = starting_amount

def play_another():
    play_again = input("Would you like to play again Y/n?: ")
    if play_again == "n":
        return False
    return True


def deal_cards():
    # Fix duplicate cards later.
    players = random.sample(deck, 2)
    computers = random.sample(deck, 2)
    return players, computers


def calculate_total(cards: list) -> int:
    """
    Calculates current score
    """

    values = [x["value"] for x in cards]

    if 11 in values and sum(values) > 21:
        values.remove(11)
        values.append(1)

    return sum(values)

def print_card(cards):
    """
    prints cards on the same line in pretty format.
    """
    pass

while continue_playing and current_amount > 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    show_balance = input("Would you like to check your account balance Y/n?: ")
    if show_balance != "n":
        print(f"Your balance is ${current_amount}")

    bet = int(input("How much would you like to bet?: $"))

    # Can't bet more than they have left.
    if bet > current_amount:
        print("\n Sorry, you do not have the funds for this. You have ${current_amount} remaining.")
        continue_playing = play_another()
        continue

    player, computer = deal_cards()

    print("=" * 100)
    print("Computers Cards: ")
    print_cards(2, [computer[0], HIDDEN_CARD])
    print("=" * 100)

    print("\n Your cards: ")
    print_cards(2, player)
    print("=" * 100)
    
    comp_total = calculate_total(computer)

    stick_or_twist = True
    if calculate_total(player) == 21:
        stick_or_twist = False
        print("21! You win")
        current_amount += bet
        stick_or_twist = False

    while stick_or_twist:
            
        choice = input("Do you want to twist Y/n?: ")
        if choice == "n":
            stick_or_twist = False
        else:
            new_card = random.sample(deck, 1)
            player.append(new_card[0])
            print("Your cards: ")
            print_cards(len(player), player)
            print("=" * 100)
            total = calculate_total(player)
            
            if total > 21:
                print("BUST - You lose")
                current_amount -= bet
                stick_or_twist = False

            elif total == 21:
                print("21! You win")
                current_amount += bet
                stick_or_twist = False
            else:
                print(f"Your current total is {total}")

    result_complete = False
    print("Computers cards: ")
    print_cards(2, computer)
    if calculate_total(player) == 21 or calculate_total(player) > 21:
        result_complete = True
    while not result_complete:
        if comp_total > 21:
            print("You win - computer is bust!")
            current_amount += bet
            result_complete = True

        elif comp_total > calculate_total(player):
            print("\n You lose!")
            current_amount -= bet
            result_complete = True

        elif comp_total < calculate_total(player) or comp_total == calculate_total(player):
            time.sleep(1)
            new_card = random.sample(deck, 1)
            computer.append(new_card[0])
            print("Computers Cards: ")
            print_cards(len(computer), computer)
            comp_total = calculate_total(computer)



    # Exit if no money remaining.
    if current_amount == 0:
        break
    continue_playing = play_another()
    

if starting_amount < current_amount:
    print(f"Well done, you're leaving with more money. You made ${current_amount-starting_amount}!!")
else:
    print(f"Unlucky, you're leaving with less money. You lost ${abs(current_amount-starting_amount)}!!")