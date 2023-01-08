# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 22:17:30 2022

@author: polyt
"""

import pandas as pd


dataframe = pd.read_excel("C:/Users/polyt/Desktop/dataframe_with_queries.xls").take([2,7,12], axis=1)
users = dataframe[
    (dataframe['Πόσο συχνά λαμβάνετε συμπληρώματα διατροφής κατά τον τελευταίο χρόνο;'] == "Σε τακτική βάση") |
    (dataframe['Πόσο συχνά λαμβάνετε συμπληρώματα διατροφής κατά τον τελευταίο χρόνο;'] == "Κάποιες φορές")]

w18 = users.loc[dataframe['Ηλικία'] == '18-25']
w26 = users.loc[dataframe['Ηλικία'] == '26-35']
w36 = users.loc[dataframe['Ηλικία'] == '36-45']
w46 = users.loc[dataframe['Ηλικία'] == '46-55']
w56 = users.loc[dataframe['Ηλικία'] == '56-65']
w65 = users.loc[dataframe['Ηλικία'] == '>65']


results18 = w18.groupby([
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;'
    ]).size()
w18_percent = results18 * 100.0 / results18.sum()

results26 = w26.groupby([
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;'
    ]).size()
w26_percent = results26 * 100.0 / results26.sum()

results36 = w36.groupby([
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;'
    ]).size()
w36_percent = results36 * 100.0 / results36.sum()

results46 = w46.groupby([
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;'
    ]).size()
w46_percent = results46 * 100.0 / results46.sum()

results56 = w56.groupby([
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;'
    ]).size()
w56_percent = results56 * 100.0 / results56.sum()

results65 = w65.groupby([
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;'
    ]).size()
w65_percent = results65 * 100.0 / results65.sum()