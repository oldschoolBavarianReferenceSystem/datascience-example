#!/usr/bin/python3

# Work with sirname data from Berlin.

import pandas as pd
import numpy as np

from pandas import Series, DataFrame

# Source: https://de.wikipedia.org/wiki/Verwaltungsgliederung_Berlins
bezirke = ['Mitte',
           'Friedrichshain-Kreuzberg',
           'Pankow',
           'Charlottenburg-Wilmersdorf',
           'Spandau',
           'Steglitz-Zehlendorf',
           'Tempelhof-Schöneberg',
           'Neukölln',
           'Treptow-Köpenick',
           'Marzahn-Hellersdorf',
           'Lichtenberg',
           'Reinickendorf'
           ]

bezirke_filenames = ['mitte.csv',
                     'friedrichshain-kreuzberg.csv',
                     'pankow.csv',
                     'charlottenburg-wilmersdorf.csv',
                     'spandau.csv',
                     'steglitz-zehlendorf.csv',
                     'tempelhof-schoeneberg.csv',
                     'neukoelln.csv',
                     'treptow-koepenick.csv',
                     'marzahn-hellersdorf.csv',
                     'lichtenberg.csv',
                     'reinickendorf.csv'
                     ]



                     



#csv = pd.read_csv("berlin/2022/")

prefix="data/berlin"
years=range(2012,2023)

for y in years:
    print(y)

for i in range(len(bezirke)):
    print(str(i+1) + ": " + bezirke[i] + ' -> ' + bezirke_filenames[i])

print("-------------------------------------")
print("")

df = pd.read_csv(prefix + "/" + str(2022) + "/" + "mitte.csv")

print(df.describe())
print(df.head())

print("")
print("Rangliste der ersten Vornamen:")
print("-------------------------------------")
print("")

