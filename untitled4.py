# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 04:56:44 2022

@author: polyt
"""

import pandas as pd


dataframe = pd.read_excel("C:/Users/polyt/Desktop/dataframe_with_queries.xls").take([2,15], axis=1)

w18 = dataframe.loc[dataframe['Ηλικία'] == '18-25']
w26 = dataframe.loc[dataframe['Ηλικία'] == '26-35']
w36 = dataframe.loc[dataframe['Ηλικία'] == '36-45']
w46 = dataframe.loc[dataframe['Ηλικία'] == '46-55']
w56 = dataframe.loc[dataframe['Ηλικία'] == '56-65']
w65 = dataframe.loc[dataframe['Ηλικία'] == '>65']


data14 = w65.take([1], axis=1)
data14_all = []

for i in range(0, 5):
    val = data14.iloc[i][0]
    parts = val.split(';')
    for part in parts:
        first = part.split("(")[0].strip()
        data14_all.append(first)

filtered14 = list(filter(lambda x: len(x) > 0, data14_all))

newdata14 = pd.DataFrame(filtered14)
result = newdata14.groupby([0]).size()
percentage = result * 100.0 / result.sum()