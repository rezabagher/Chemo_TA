# -*- coding: utf-8 -*-
"""pls_da.ipynb
"""

from google.colab import files
uploaded = files.upload()

from sklearn.cross_decomposition import PLSRegression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv("data.csv")


df.drop(columns=['Unnamed: 32'], inplace=True)
df.drop(columns=['id'], inplace=True)

df = df.dropna()

df['diagnosis'].value_counts()['B']

x = df.drop(columns=['diagnosis'])
y = df['diagnosis'].apply(lambda x: 0 if x=="B" else 1 )

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

pls = PLSRegression(n_components=2)

pls.fit(x_train, y_train)

y_pred = pls.predict(x_test)

pls.score(x_test, y_test)

from sklearn import preprocessing

np.mean(y_pred)

def prepr(x):
  for i in range(len(x)):
    (x[i]-np.mean(x))/(max(x)-min(x))
  return x

#PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=1)
df_3d = pca.fit_transform(x_train)

df_3d=df_3d.flatten()

x_test_p = pca.transform(x_test)

x_test_pf=x_test_p.flatten()

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df_3d and y_train are available dataframes/arrays
# Plot a strip plot using seaborn
sns.stripplot(x=df_3d, y=y_train)
plt.show()

# Assuming df_3d and y_train are available dataframes/arrays
# Plot a strip plot using seaborn
sns.stripplot(x=x_test_pf, y=y_pred_f)
plt.show()

y_pred_f=y_pred.flatten()
y_pred_f

for i in range(len(y_pred_f)):
    if y_pred_f[i]<=0.5:
      y_pred_f[i] = 0
    else :
       y_pred_f[i]=1

y_pred_f

from  pandas import DataFrame

y_pred_p = DataFrame(y_pred_f, columns=["pred"])
y_pred_p

from sklearn.metrics import accuracy_score
print(accuracy_score( y_test, y_pred_p))
