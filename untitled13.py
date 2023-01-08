# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 08:39:58 2022

@author: polyt
"""

import pandas as pd


dataframe = pd.read_excel("C:/Users/polyt/Desktop/dataframe_with_queries.xls").take([2,24], axis=1)

w18 = dataframe.loc[dataframe['Ηλικία'] == '18-25']
w26 = dataframe.loc[dataframe['Ηλικία'] == '26-35']
w36 = dataframe.loc[dataframe['Ηλικία'] == '36-45']
w46 = dataframe.loc[dataframe['Ηλικία'] == '46-55']
w56 = dataframe.loc[dataframe['Ηλικία'] == '56-65']
w65 = dataframe.loc[dataframe['Ηλικία'] == '>65']


results18 = w18.groupby([
    'Κατά την εκτίμησή σας, πόσο ενημερωμένος -η είστε σχετικά με τα συμπληρώματα διατροφής;'
    ]).size()
w18_percent = results18 * 100.0 / results18.sum()

results26 = w26.groupby([
    'Κατά την εκτίμησή σας, πόσο ενημερωμένος -η είστε σχετικά με τα συμπληρώματα διατροφής;'
    ]).size()
w26_percent = results26 * 100.0 / results26.sum()

results36 = w36.groupby([
    'Κατά την εκτίμησή σας, πόσο ενημερωμένος -η είστε σχετικά με τα συμπληρώματα διατροφής;'
    ]).size()
w36_percent = results36 * 100.0 / results36.sum()

results46 = w46.groupby([
    'Κατά την εκτίμησή σας, πόσο ενημερωμένος -η είστε σχετικά με τα συμπληρώματα διατροφής;'
    ]).size()
w46_percent = results46 * 100.0 / results46.sum()

results56 = w56.groupby([
    'Κατά την εκτίμησή σας, πόσο ενημερωμένος -η είστε σχετικά με τα συμπληρώματα διατροφής;'
    ]).size()
w56_percent = results56 * 100.0 / results56.sum()

results65 = w65.groupby([
    'Κατά την εκτίμησή σας, πόσο ενημερωμένος -η είστε σχετικά με τα συμπληρώματα διατροφής;'
    ]).size()
w65_percent = results65 * 100.0 / results65.sum()