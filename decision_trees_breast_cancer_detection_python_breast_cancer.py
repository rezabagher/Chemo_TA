# -*- coding: utf-8 -*-
"""Decision Trees - Breast Cancer Detection Python_Breast Cancer.ipynb




"""

from google.colab import files
uploaded = files.upload()

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report

df = pd.read_csv("data.csv")
df

df.drop(columns=['Unnamed: 32'], inplace=True)

df

df = df.dropna()

df['diagnosis'].value_counts()['B']

x = df.drop(columns=['diagnosis'])
y = df['diagnosis'].apply(lambda x: 0 if x=="B" else 1 )

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(random_state=0)

cross_val_score(clf, x_train, y_train, cv=10)

clf = DecisionTreeClassifier(random_state=0)

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print(classification_report(y_test, y_pred))

