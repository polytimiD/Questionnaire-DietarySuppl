# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 21:50:20 2022

@author: polyt
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap

dataframe = pd.read_excel("C:/Users/polyt/Desktop/dataframe_with_queries.xls")

# print (dataframe)

# residence = dataframe.take([3], axis=1)
# residence_plotdf = residence.groupby(residence.columns[0]).size()

# #define Seaborn color palette to use
# colors = sns.color_palette('colorblind')


# #create pie chart
# #plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
# plt.pie(residence_plotdf, colors=colors, labels=residence_plotdf.index)
# plt.show()

def pretty_name(text):
    wrapper = textwrap.TextWrapper()
    result = '\n'.join(textwrap.wrap(text, width=35))
    # print(result)
    return result

# def fix5(inputdf, keepValues):
    


def pieFunc(inputDataframe, index):
    workingSet = inputDataframe.take([index], axis=1)
    
    plotData = workingSet.groupby(workingSet.columns[0]).size()
    
    #define Seaborn color palette to use
    colors = sns.color_palette('colorblind')
    
    
    plt.pie(plotData, colors=colors, labels=plotData.index, autopct='%.2f%%')
    # plt.legend()
    plt.title(label=pretty_name(workingSet.columns[0]), wrap=True)

    plt.savefig("fig_" + str(index) + ".svg", bbox_inches="tight")
    plt.close()
    plt.cla()
    plt.clf()
    # plt.show()
    


def pie5(dataframe):
    
    data5 = dataframe.take([5], axis=1)
    for i in range(0, 482):
        val = data5.iloc[i][0]
        if(not(val in ['Μεσογειακή', 'Παμφαγική', 'Χορτοφαγική', 'Vegan'])):
            data5.iloc[i][0] = 'Άλλο'
            # print(i)
            
    plotData = data5.groupby(data5.columns[0]).size()
    
    plotData2 = plotData.reindex(['Vegan', 'Μεσογειακή', 'Άλλο', 'Χορτοφαγική', 'Παμφαγική'])
    
    colors = sns.color_palette('colorblind')
    plt.pie(plotData2, colors=colors, labels=plotData2.index, autopct='%.2f%%')
    plt.title(label=pretty_name(data5.columns[0]), wrap=True)  
    plt.savefig("fig_5.svg", bbox_inches="tight")
    plt.close()
    plt.cla()
    plt.clf()
        
    
    
    
    
    
    
    
# pieFunc(dataframe, 1)
# pieFunc(dataframe, 2)
# pieFunc(dataframe, 3)
# pieFunc(dataframe, 4)
# pie5(dataframe)
# pieFunc(dataframe, 6)
# pieFunc(dataframe, 7)
# pieFunc(dataframe, 8)
# pieFunc(dataframe, 9)
# pieFunc(dataframe, 10)
# pieFunc(dataframe, 11)
# pieFunc(dataframe, 12)
# pieFunc(dataframe, 17)
# pieFunc(dataframe, 18)
# pieFunc(dataframe, 19)
# pieFunc(dataframe, 20)
# pieFunc(dataframe, 21)
# pieFunc(dataframe, 22)
# pieFunc(dataframe, 23)
# pieFunc(dataframe, 24)
# pieFunc(dataframe, 25)


data13 = dataframe.take([13], axis=1)
data13_all = []

for i in range(0, 482):
    val = data13.replace("\xa0", " ").iloc[i][0]
    parts = val.split(';')
    for part in parts:
        first = part.split("(")[0].strip()
        if(first == "Βιταμίνη D"):
            first = "Βιταμίνες"
        if(first == "Κουρκουμίνη"):
            first = "Βότανα και φυτικά συμπληρώματα"
        if(first == "Καφεΐνη"):
            first = "Βότανα και φυτικά συμπληρώματα"
        if(first == "Σιδηρο"):
            first = "Ιχνοστοιχεία και μέταλλα"
        if(first == "Προϊόν ζύμωσης"):
            first = "Προβιοτικά ή/και προεβιοτικά"
        if(first == "Χονδροπροστατευτικά"):
            first = "Γυμναστηριακά σκευάσματα"
        if(first == "βιταμίνη C"):
            first = "Αντιοξειδωτικά"
            
        data13_all.append(first)

filtered13 = list(filter(lambda x: len(x) > 0, data13_all))


df13 = pd.DataFrame(data = filtered13, columns=data13.columns)
group13 = df13.groupby(df13.columns[0]).size().reindex([
    "Αντιοξειδωτικά",
    "Βιταμίνες",
    "Βότανα και φυτικά συμπληρώματα",
    "Γυμναστηριακά σκευάσματα",
    "Λιπαρά οξέα",
    "Ιχνοστοιχεία και μέταλλα",
    "Κανένα από τα παραπάνω",
    "Πολυβιταμινούχα σκευάσματα",
    "Προβιοτικά ή/και προεβιοτικά",
    "Πρωτεΐνες",
    ])


colors = sns.color_palette('colorblind')
plt.pie(group13, colors=colors, labels=group13.index, autopct='%.2f%%')
plt.title(label=pretty_name(df13.columns[0]), wrap=True)  
plt.savefig("fig_13.svg", bbox_inches="tight")
plt.close()
plt.cla()
plt.clf()






data14 = dataframe.take([14], axis=1)
data14_all = []

for i in range(0, 482):
    val = data14.iloc[i][0]
    parts = val.split(';')
    for part in parts:
        first = part.split("(")[0].strip()
        data14_all.append(first)

filtered14 = list(filter(lambda x: len(x) > 0, data14_all))


df14 = pd.DataFrame(data = filtered14, columns=data14.columns)
group14 = df14.groupby(df14.columns[0]).size().reindex([
    'Τίποτα από τα παραπάνω, έχω χρησιμοποιήσει συμπληρώματα διατροφής από απλή περιέργεια',
    'Πειραματικά',
    'Ενίσχυση της αποκατάστασης μετά τη φυσική άσκηση',
    'Ενίσχυση διατροφής λόγω αλλαγής των διατροφικών συνηθειών',
    'Ενίσχυση άλλης λαμβανόμενης φαρμακευτικής ουσίας',
    'Βελτίωση απόδοσης κατά τη φυσική άσκηση',
    'Βελτίωση ύπνου',
    'Ενίσχυση αισθητικών χαρακτηριστικών',
    'Βελτίωση και ενίσχυση ψυχικής υγείας',
    'Δεν χρησιμοποιώ συμπληρώματα διατροφής',
    'Βελτίωση ή αποκατάσταση κάποιου βιολογικού δείκτη ή βιολογικής λειτουργίας',
    'Διατήρηση υγείας και ευεξίας',
    'Ενίσχυση του ανοσοποιητικού συστήματος'])

x14 = group14.index
y14 = group14.values
y14float = []

for i in range(0, 13):
    y14float.append(100.0*y14[i]/482.0)
    

# print(x14[2])
print(y14float)

# plt.pie(group14, colors=colors, labels=group14.index, autopct='%.2f%%')
# plt.bar(group14, height=150, colors=colors, labels=group14.index)
hbars14 = plt.barh(y=x14, width=y14float, color=colors)
plt.bar_label(hbars14, fmt='%.2f%%')
plt.title(label=pretty_name(df14.columns[0]), wrap=True)
# plt.show()
plt.savefig("fig_14.svg", bbox_inches="tight")
plt.close()
plt.cla()
plt.clf()







data15 = dataframe.take([15], axis=1)
data15_all = []

for i in range(0, 482):
    val = data15.iloc[i][0]
    parts = val.split(';')
    for part in parts:
        first = part.split("(")[0].strip()
        if(first in ["Γιατρος που ειναι και στενος φιλος",
                     "Δε λαμβάνω συμπληρώματα διατροφής",
                     "Δεν χρησιμοποιώ",
                     "Είμαι γυμναστής με μεταπτυχιακό στην αθλητική διατροφή",
                     "Ειμαι διατροφολογος",
                     "Μου τα χάρισαν",
                     "Προσωπική αναζήτηση και ενημέρωση",
                     "Σπουδάζω πάνω στο αντικείμενο",
                     "Από τις συσκευασίες των προϊόντων",
                     "Από κανένα",
                     "Σχετικές επιστημονικές έρευνες"]):
            first = "Άλλο"
        data15_all.append(first)

filtered15 = list(filter(lambda x: len(x) > 0, data15_all))


df15 = pd.DataFrame(data = filtered15, columns=data15.columns)
group15 = df15.groupby(df15.columns[0]).size().reindex([
    'Άλλο',
    'Από επαγγελματία στο χώρο της αισθητικής',
    'Από σύμβουλο ευεξίας και αυτοβελτίωσης',
    'Από το γυμναστή μου',
    'Από τα μέσα μαζικής ενημέρωσης',
    'Από διαφημίσεις',
    'Από το διαιτολόγο μου',
    'Από τον κοινωνικό μου κύκλο',
    'Από το φαρμακοποιό μου',
    'Από το διαδίκτυο',
    'Από το γιατρό μου'])

x15 = group15.index
y15 = group15.values
y15float = []
for i in range(0, 11):
    y15float.append(100.0*y15[i]/482.0)

hbars15 = plt.barh(y=x15, width=y15float, color=colors)
plt.bar_label(hbars15, fmt='%.2f%%')
plt.title(label=pretty_name(df15.columns[0]), wrap=True)
# plt.show()
plt.savefig("fig_15.svg", bbox_inches="tight")
plt.close()
plt.cla()
plt.clf()












data16 = dataframe.take([16], axis=1)
data16_all = []

for i in range(0, 482):
    val = data16.iloc[i][0]
    parts = val.split(';')
    for part in parts:
        first = part.split("(")[0].strip()
        if(first in ["Από Αλληλεγγυο κοινωνικό καταστημα",
                     "Εταιρεία που πουλάει δικά της συμπληρώματα διατροφής"]):
            first = "Άλλο"
        data16_all.append(first)

filtered16 = list(filter(lambda x: len(x) > 0, data16_all))


df16 = pd.DataFrame(data = filtered16, columns=data16.columns)
group16 = df16.groupby(df16.columns[0]).size().reindex([
    'Άλλο',
    'Από κέντρο αισθητικής',
    'Από το γυμναστήριο',
    'Από υπαίθριες αγορές',
    'Από τον κοινωνικό μου κύκλο',
    'Καλλιεργώ και καταναλώνω δικά μου βότανα ως συμπληρώματα διατροφής',
    'Από επαγγελματία στο χώρο της άθλησης ή της συμβουλευτικής ευεξίας και αυτοβελτίωσης',
    'Από πρατήρια βιολογικών προϊόντων',
    'Από το σούπερ μάρκετ',
    'Δεν καταναλώνω συμπληρώματα διατροφής',
    'Από το διαδίκτυο',
    'Από το φαρμακείο'
    ])

x16 = group16.index
y16 = group16.values
y16float = []
for i in range(0, 12):
    y16float.append(100.0*y16[i]/482.0)

hbars16 = plt.barh(y=x16, width=y16float, color=colors)
plt.bar_label(hbars16, fmt='%.2f%%')
plt.title(label=pretty_name(df16.columns[0]), wrap=True)
# plt.show()
plt.savefig("fig_16.svg", bbox_inches="tight")
plt.close()
plt.cla()
plt.clf()























print("done")