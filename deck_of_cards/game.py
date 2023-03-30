from classes.deck import Deck

bicycle = Deck()

bicycle.show_cards()

from classes.deck import Deck
import random

bicycle = Deck()


class Game:
    sum_of_cards = 0
    cards_list = []

    def __init__(self) :
        pass

    @staticmethod
    def random_cards():
        # get random cards and values
        random_card = random.randint(1,12)
        return random_card
        
    @classmethod
    def draw_card(cls):
        # add the cards to the cards array
        # update new cards values
        new_card = cls.random_cards()
        cls.cards_list.append(new_card)
        cls.sum_of_cards = cls.sum_of_cards + new_card
        if cls.sum_of_cards < 21:
            response = input(f"You now have {cls.sum_of_cards}, would you like another card ?")
            if response.lower == "yes":
                cls.draw_card()
        elif cls.sum_of_cards == 21:
            print("You have BlackJack!!!")
        else:
            print("Sorry you're a LOSER !!!")
            response = input("would you like to play a new game ?")
            if response.lower() == "yes":
                cls.start_game()

    @classmethod
    def start_game(cls):
    #     # draw two random cards 
    #     # create new cards array
    #     # combine the values of the two cards
    #     # display the combined svalues of the cards
        card1 = cls.random_cards()
        card2 = cls.random_cards()
        cls.cards_list.append(card1)
        cls.cards_list.append(card2)
        cls.sum_of_cards = card1 + card2
        if cls.sum_of_cards == 21:
            print("Wow you got Black!!!")
        else:
            response = input(f"Hey, you're at {cls.sum_of_cards} would you like another card?")
            if response.lower() == "yes":
                cls.draw_card()


Game.start_game()