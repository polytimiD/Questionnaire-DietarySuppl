# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 04:14:18 2022

@author: polyt
"""

import pandas as pd


dataframe = pd.read_excel("C:/Users/polyt/Desktop/dataframe_with_queries.xls").take([2, 12, 14], axis=1)

users = dataframe[
    (dataframe['Πόσο συχνά λαμβάνετε συμπληρώματα διατροφής κατά τον τελευταίο χρόνο;'] == "Σε τακτική βάση") |
    (dataframe['Πόσο συχνά λαμβάνετε συμπληρώματα διατροφής κατά τον τελευταίο χρόνο;'] == "Κάποιες φορές")]

w18 = users.loc[users['Ηλικία'] == '18-25']
w26 = users.loc[users['Ηλικία'] == '26-35']
w36 = users.loc[users['Ηλικία'] == '36-45']
w46 = users.loc[users['Ηλικία'] == '46-55']
w56 = users.loc[users['Ηλικία'] == '56-65']
w65 = users.loc[users['Ηλικία'] == '>65']


data14 = w65.take([2], axis=1)
data14_all = []

for i in range(0, 2):
    val = data14.iloc[i][0]
    parts = val.split(';')
    for part in parts:
        first = part.split("(")[0].strip()
        data14_all.append(first)

filtered14 = list(filter(lambda x: len(x) > 0, data14_all))

newdata14 = pd.DataFrame(filtered14)
result = newdata14.groupby([0]).size()
percentage = result * 100.0 / result.sum()