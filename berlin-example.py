#!/usr/bin/python3

# Work with sirname data from Berlin.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from pandas import Series, DataFrame

# Source of districts: https://de.wikipedia.org/wiki/Verwaltungsgliederung_Berlins
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

# Read one example dataset:
df = pd.read_csv(prefix + "/" + str(2022) + "/" + "mitte.csv")

print(df.describe())
print(df.head())

print("")
print("Rangliste der ersten Vornamen:")
print("-------------------------------------")
print("")

girls_firstname = df[(df.geschlecht=='w') & (df.position==1)]
girls_firstname = girls_firstname.sort_values(by=['anzahl', 'vorname'], ascending=[False, True])

sum = girls_firstname['anzahl'].sum()

girls_firstname['promille']=girls_firstname['anzahl']*1000/sum
print("Alle Girls Firstname: " + str(sum))
print(girls_firstname.describe())
print(girls_firstname.head(20))

top20=girls_firstname.head(20)

top20.plot()

#matplotlib.use('gtk4agg') #qtagg')
#matplotlib.use('qtagg')
#plt.show()

##plt.savefig('berlin.png', format='png')
