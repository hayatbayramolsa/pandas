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


# %% Filtering

# maaşı 200'den fazla olanlar
filtre1 = dataFrame1.MAAS > 200

type(filtre1)

filtrelenmis_data = dataFrame1[filtre1]

# hem o hem de yaşı 20'den küçük olanlar
filtre2 = dataFrame1.AGE < 20

dataFrame1[filtre1 & filtre2]


# yaşı 30'un üstünde olanlar
dataFrame1[dataFrame1.AGE > 30]


# adı Mustafa olan
dataFrame1[dataFrame1.NAME == "Mustafa"]


# mustafa veya büşra olan
dataFrame1[(dataFrame1.NAME == "Mustafa") | (dataFrame1.NAME == "Büşra")]


# %% List Comprehension

# ortalama maaş
dataFrame1.MAAS

ortalama_maas = dataFrame1.MAAS.mean()


# numpy ile bulma
import numpy as np

ortalama_maas_np = np.mean(dataFrame1.MAAS)



# seviyelerine göre string ekleme

for i in dataFrame1.MAAS:
    print(i)

for i in dataFrame1.MAAS:
    if(i > ortalama_maas):
        print("yüksek")
    else:
        print("düşük")
        

dataFrame1["seviye"] = ["yüksek" if i > ortalama_maas else "düşük" for i in dataFrame1.MAAS]


# sütunları küçük harfe çevirme

dataFrame1.columns

"ENES".lower()

dataFrame1.columns = [i.lower() for i in dataFrame1.columns]


# boşlukları yok etme

len("yapay zeka".split()) 

dataFrame1.columns = [i.split()[0] + "_" + i.split()[1]  if(len(i.split())) > 1 else i for i in dataFrame1.columns]


# %% drop and concatenating

dataFrame1.drop(["yeni feature"], axis=1, inplace=True)


# concatenate

data1 = dataFrame1.head()
data2 = dataFrame1.tail()


# vertical
data_concat = pd.concat([data1, data2], axis=0)

# horizontal
maas = dataFrame1.maas
yas = dataFrame1.age

h_concat = pd.concat([maas, yas], axis=1)



# %% transforming data

dataFrame1["list_comp"] = [i*2 for i in dataFrame1.age]


# apply yöntemi


def multiply(age):
    return age*2


dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)
