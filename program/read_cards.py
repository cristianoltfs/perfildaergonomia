import pandas as pd

def read_cards():
    cards = pd.read_csv('data/cartas.csv', sep=';')
    return cards