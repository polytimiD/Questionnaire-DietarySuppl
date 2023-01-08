# Questionnaire-DietarySuppl

Code for the analysis of questionnaire data for academic research work, concerning the usage of dietary supplements.

- Implementation language: Python.
- Libraries used: pandas, matplotlib, seaborn.
- Dataset: 2-dimensional matrix of 25 questions, answered by 482 participants. Checkbox question options are separated by commas.

- Type of data imput -
The questionnaire includes closed-ended questions of the following types: dichotomous, multiple-choice and checkbox.

- Data Cleansing -
When questions allowed the input of some other answer, data cleansing was applied for the calculation of percentages and the creation of the graphical representations of the data. The aim of the data cleansing is that the data visualizations adhere to the original questions and answers of the questionnaires. Thus, when the participants did not choose one of the answers that the researcher provided, then the new answer was categorized as "Other". If the new answer fits well in one of the available categories, then the answer is considered as of this category.
The decision for applying data cleansing is justified by the rather sparse incidence of such data, meaning that it did not distort in any case the observed motifs in the answers of the participants.

- Data Visualization -
Pie charts for dichotomous and multiple choice questions.
Bar charts for checkbox questions.
Seaborn color_palette("coloblind")

- Data analysis -
The data are inserted in a 2-dimensional data structure, namely a dataframe of the pandas library.
The data analysis is mostly conducted according to the age groups that were determined from one of the demographical questions of the questionnaire.
One or more questions were combined in order to calculate percentages of participants, according to the research inquiries of the investigator.

(The research questions are in greek language. The dataset is not provided here, because it is part of unpublished research work.)
