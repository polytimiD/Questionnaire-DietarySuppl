# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 21:23:59 2022

@author: polyt
"""

import pandas as pd


dataframe = pd.read_excel("C:/Users/polyt/Desktop/dataframe_with_queries.xls")

# Question 1
dataframe1 = dataframe.take([1,2,3,4,7,10,12], axis=1)

# suppl_sex = dataframe1.groupby(dataframe1.columns[0]).size()
# suppl_age = dataframe1.groupby(dataframe1.columns[1]).size()
# suppl_loc = dataframe1.groupby(dataframe1.columns[2]).size()
# suppl_edu = dataframe1.groupby(dataframe1.columns[3]).size()
# suppl_diet = dataframe1.groupby(dataframe1.columns[4]).size()
# suppl_qual = dataframe1.groupby(dataframe1.columns[5]).size()
# suppl_freq = dataframe1.groupby(dataframe1.columns[6]).size()

# supplement_users_always = dataframe1.loc[(dataframe1['Πόσο συχνά λαμβάνετε συμπληρώματα διατροφής κατά τον τελευταίο χρόνο;'] == "Σε τακτική βάση") or (dataframe1['Πόσο συχνά λαμβάνετε συμπληρώματα διατροφής κατά τον τελευταίο χρόνο;'] == "Κάποιες φορές")]supplement_users_sometimes = dataframe1.loc[dataframe1['Πόσο συχνά λαμβάνετε συμπληρώματα διατροφής κατά τον τελευταίο χρόνο;'] == "Κάποιες φορές"]
suppl_users = dataframe1[
    (dataframe1['Πόσο συχνά λαμβάνετε συμπληρώματα διατροφής κατά τον τελευταίο χρόνο;'] == "Σε τακτική βάση") |
    (dataframe1['Πόσο συχνά λαμβάνετε συμπληρώματα διατροφής κατά τον τελευταίο χρόνο;'] == "Κάποιες φορές") ]

# women_users = suppl_users[suppl_users['Φύλο'] == "Γυναίκα"]
# men_users = suppl_users[suppl_users['Φύλο'] == "Άνδρας"]
users_grouping = suppl_users.groupby([
    'Φύλο',
    'Ηλικία',
    # 'Τόπος κατοικίας',
    'Ανώτατο επίπεδο εκπαίδευσης που έχετε ολοκληρώσει',
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;',
    # 'Πως θα περιγράφατε συνολικά την καθημερινότητά σας, σε επίπεδο διαβίωσης και ποιότητας ζωής;'
    ]).size()

w18 = suppl_users.loc[suppl_users['Ηλικία'] == '18-25']
w26 = suppl_users.loc[suppl_users['Ηλικία'] == '26-35']
w36 = suppl_users.loc[suppl_users['Ηλικία'] == '36-45']
w46 = suppl_users.loc[suppl_users['Ηλικία'] == '46-55']
w56 = suppl_users.loc[suppl_users['Ηλικία'] == '56-65']
w65 = suppl_users.loc[suppl_users['Ηλικία'] == '>65']

w18 = w18.groupby([
    'Φύλο',
    'Τόπος κατοικίας',
    # 'Ανώτατο επίπεδο εκπαίδευσης που έχετε ολοκληρώσει',
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;',
    # 'Πως θα περιγράφατε συνολικά την καθημερινότητά σας, σε επίπεδο διαβίωσης και ποιότητας ζωής;'
    ]).size()

w18_percent = w18 * 100.0 / w18.sum()


w26 = w26.groupby([
    'Τόπος κατοικίας',
    # 'Ανώτατο επίπεδο εκπαίδευσης που έχετε ολοκληρώσει',
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;',
    # 'Πως θα περιγράφατε συνολικά την καθημερινότητά σας, σε επίπεδο διαβίωσης και ποιότητας ζωής;'
    ]).size()

w26_percent = w26 * 100.0 / w26.sum()


w36 = w36.groupby([
    'Τόπος κατοικίας',
    # 'Ανώτατο επίπεδο εκπαίδευσης που έχετε ολοκληρώσει',
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;',
    # 'Πως θα περιγράφατε συνολικά την καθημερινότητά σας, σε επίπεδο διαβίωσης και ποιότητας ζωής;'
    ]).size()

w36_percent = w36 * 100.0 / w36.sum()


w46 = w46.groupby([
    'Τόπος κατοικίας',
    # 'Ανώτατο επίπεδο εκπαίδευσης που έχετε ολοκληρώσει',
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;',
    # 'Πως θα περιγράφατε συνολικά την καθημερινότητά σας, σε επίπεδο διαβίωσης και ποιότητας ζωής;'
    ]).size()

w46_percent = w46 * 100.0 / w46.sum()


w56 = w56.groupby([
    'Τόπος κατοικίας',
    # 'Ανώτατο επίπεδο εκπαίδευσης που έχετε ολοκληρώσει',
    'Πως θα χαρακτηρίζατε συνολικά τις διατροφικές σας επιλογές;',
    # 'Πως θα περιγράφατε συνολικά την καθημερινότητά σας, σε επίπεδο διαβίωσης και ποιότητας ζωής;'
    ]).size()

w56_percent = w56 * 100.0 / w56.sum()





# men_users = suppl_users[suppl_users['Φύλο'] == "Άνδρας"]

# m18 = men_users.loc[men_users['Ηλικία'] == '18-25']
# m26 = men_users.loc[men_users['Ηλικία'] == '26-35']
# m36 = men_users.loc[men_users['Ηλικία'] == '36-45']
# m46 = men_users.loc[men_users['Ηλικία'] == '46-55']
# m56 = men_users.loc[men_users['Ηλικία'] == '56-65']


