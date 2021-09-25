import socket
import threading
import pandas as pd
from random import sample
import _pickle as cPickle
cartas = pd.read_csv('cartas.csv', sep=';')

carta = cartas.loc[1]

carta1= carta.apply(str)


carta= carta.values.astype(str)
print(carta)
