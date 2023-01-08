# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 03:58:22 2022

@author: polyt
"""

import pandas as pd


dataframe = pd.read_excel("C:/Users/polyt/Desktop/dataframe_with_queries.xls").take([5, 12 ], axis=1)

vegan = dataframe[(dataframe['Ποιος τύπος διατροφής περιγράφει καλύτερα τις καθημερινές σας συνήθειες;'] == "Vegan")]
    

veganGroups = vegan.groupby(['Πόσο συχνά λαμβάνετε συμπληρώματα διατροφής κατά τον τελευταίο χρόνο;']).size()

vegan_percent = veganGroups * 100.0 / veganGroups.sum()




veget = dataframe[(dataframe['Ποιος τύπος διατροφής περιγράφει καλύτερα τις καθημερινές σας συνήθειες;'] == "Χορτοφαγική")]
    

vegetGroups = veget.groupby(['Πόσο συχνά λαμβάνετε συμπληρώματα διατροφής κατά τον τελευταίο χρόνο;']).size()

veget_percent = vegetGroups * 100.0 / grassGroups.sum()