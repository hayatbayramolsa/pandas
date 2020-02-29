# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:00:20 2020

@author: Hp 840
"""

import pandas as pd

sozluk = {"NAME": ["Ali", "Ahmet", "Ayşe", "Mustafa", "Sinan", "Zeynep", "Büşra", "Esra"],
          "AGE": [15, 17, 22, 27, 18, 20, 32, 21],
          "MAAS": [100, 150, 130, 220, 350, 120, 250, 180]}


dataFrame1 = pd.DataFrame(sozluk)

head = dataFrame1.head()
tail = dataFrame1.tail()

head = dataFrame1.head(6)

# %% Pandas Basic Methods

dataFrame1.columns

dataFrame1.info()

dataFrame1.dtypes

dataFrame1.describe() # numeric columns

# %% Indexing and Slicing

dataFrame1["NAME"]

dataFrame1.AGE

dataFrame1["yeni feature"] = [-1, -2, -3, -4, -5, -6, -7, -8]

dataFrame1.yeni Feature

dataFrame1["yeni feature"]


dataFrame1.loc[:, "AGE"]

dataFrame1.loc[:3, "AGE"]

dataFrame1.loc[:3, "AGE" : "MAAS"]

dataFrame1.loc[:3, ["AGE", "NAME"]]


dataFrame1.iloc[:, 2]






