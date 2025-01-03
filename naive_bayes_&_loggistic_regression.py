# -*- coding: utf-8 -*-
"""Naive_bayes_&_loggistic_regression.ipynb

"""

from google.colab import files
uploaded = files.upload()

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report

df = pd.read_csv("data.csv")
df

df.drop(columns=['Unnamed: 32'], inplace=True)

df.drop(columns=['id'], inplace=True)

df = df.dropna()

df['diagnosis'].value_counts()['B']

x = df.drop(columns=['diagnosis'])
y = df['diagnosis'].apply(lambda x: 0 if x=="B" else 1 )

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x_train, y_train)
y_pred_g = gnb.predict(x_test)

print(classification_report(y_test, y_pred_g))

from sklearn.linear_model import LogisticRegression
LG =  LogisticRegression(random_state=0)
LG.fit(x_train, y_train)
y_pred_L = LG.predict(x_test)
print(classification_report(y_test, y_pred_L))
