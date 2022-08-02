BLACKJACK = """
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  

"""


CARDS = "A23456789"
CARDS_LIST = [x for x in CARDS]
CARDS_LIST.append("10")
CARDS_LIST.append("J")
CARDS_LIST.append("Q")
CARDS_LIST.append("K")

HEART = "❤️"
CLUB = "♣️"
SPADE = "♠️"
DIAMOND = "♦"

suits = [HEART, CLUB, SPADE, DIAMOND]

def create_card(rank, suit, space):
    card = (
        '┌─────────┐\n'
        '│{r}{_}       │\n'
        '│         │\n'
        '│         │\n'
        '│    {s}    │\n'
        '│         │\n'
        '│         │\n'
        '│       {_}{r}│\n'
        '└─────────┘\n'
    ).format(r=rank, _=space, s=suit)
    return card

def create_card_list(rank, suit, space):
    card_list = [
        ["┌─────────┐"],
        ['│{r}{_}       │'.format(r=rank, _=space)],
        ['│         │'],
        ['│         │'],
        ['│    {s}    │'.format(s=suit)],
        ['│         │'],
        ['│         │'],
        ['│       {_}{r}│'.format(r=rank, _=space)],
        ['└─────────┘']
    ]
    return card_list


deck = []

for suit in suits:
    for card in CARDS_LIST:
        space = " "
        try:
            if int(card) == 10:
                space = ""
        except:
            pass
        new_card = create_card_list(card, suit, space)
        value = 0
        try:
            value = int(card)
        except:
            if card == "A":
                value = 11
            else:
                value = 10
        to_add = {
            "card": card,
            "suit": suit,
            "image": new_card,
            "value": value
        }
        deck.append(to_add)


HIDDEN_CARD = {
"card": "hidden",
"suit": None,
"image":[
    ['┌─────────┐'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['└─────────┘']
],
"value": 0
}


def print_cards(no_of_cards, cards):
    if no_of_cards == 1:
        print("".join(cards["image"]))
    elif no_of_cards == 2:
        card_zip = list(zip(cards[0]["image"], cards[1]["image"]))
        for layer in card_zip:
            print(f'{"".join(layer[0])} {"".join(layer[1])}')
    elif no_of_cards == 3:
        card_zip = list(zip(cards[0]["image"], cards[1]["image"],cards[2]["image"]))
        for layer in card_zip:
            print(f'{"".join(layer[0])} {"".join(layer[1])} {"".join(layer[2])}')
    elif no_of_cards == 4:
        card_zip = list(zip(cards[0]["image"], cards[1]["image"],cards[2]["image"], cards[3]["image"]))
        for layer in card_zip:
            print(f'{"".join(layer[0])} {"".join(layer[1])} {"".join(layer[2])} {"".join(layer[3])}')
    elif no_of_cards == 5:
        card_zip = list(zip(cards[0]["image"], cards[1]["image"],cards[2]["image"], cards[3]["image"], cards[4]["image"]))
        for layer in card_zip:
            print(f'{"".join(layer[0])} {"".join(layer[1])} {"".join(layer[2])} {"".join(layer[3])} {"".join(layer[4])}')
    elif no_of_cards == 6:
        card_zip = list(zip(cards[0]["image"], cards[1]["image"],cards[2]["image"], cards[3]["image"], cards[4]["image"], cards[5]["image"]))
        for layer in card_zip:
            print(f'{"".join(layer[0])} {"".join(layer[1])} {"".join(layer[2])} {"".join(layer[3])} {"".join(layer[4])} {"".join(layer[5])}')


    
    