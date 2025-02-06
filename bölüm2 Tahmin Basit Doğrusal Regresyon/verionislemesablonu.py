# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:50:13 2020

@author: sadievrenseker
"""

#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('satislar.csv')
#pd.read_csv("veriler.csv")
#test

print(veriler)

#veri ön işleme

aylar = veriler[['Aylar']]
print(aylar)

satislar = veriler[['Satislar']]
print(satislar)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(aylar,satislar,test_size=0.33,random_state=0)


from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)



















