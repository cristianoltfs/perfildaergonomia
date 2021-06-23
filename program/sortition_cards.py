import random

def sortition_cards(cards):
    var = random.randint(0,cards[cards.columns[0]].count()-1)
    print(cards.iloc[var]["categoria"])