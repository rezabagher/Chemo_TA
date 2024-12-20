# -*- coding: utf-8 -*-
"""ridge_lasso_regressions.ipynb

"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoCV, RidgeCV

from google.colab import files
uploaded = files.upload()

df = pd.read_csv("insurance.csv")
df

x = df.drop(columns=['charges'])
y = df['charges']

x_seen, x_test, y_seen, y_test = train_test_split(x, y, test_size=0.2, random_state=50)

x_seen['smoker'] = x_seen['smoker'].apply(lambda x: 0 if x=='no' else 1)

def SX(x):
  if x == "female":
    return 0
  else:
    return  1

x_seen['sex'] = x_seen['sex'].apply(SX)

x_seen

x_seen["region"].unique()

def RG(j):
  if j == 'northwest':
    return 0
  elif j ==  'southwest':
    return 1
  elif j == 'southeast':
    return 2
  elif j == 'northeast':
    return 3

x_seen["region"]=x_seen["region"].apply(RG)

x_seen

"""#training
#cross validation and regression
"""

#ridge and lasso regression
alphas = np.logspace(-6, 2, 100)
reg_lasso = LassoCV(alphas=alphas, cv=5, random_state=0).fit(x_seen, y_seen)
reg_ridge = RidgeCV(alphas=alphas, cv=5).fit(x_seen, y_seen)

reg_lasso.alpha_

reg_ridge.alpha_

"""evaluation

"""

x_test["smoker"] = x_test['smoker'].apply(lambda x: 0 if x=='no' else 1)
x_test["sex"] = x_test['sex'].apply(SX)
x_test["region"]=x_test["region"].apply(RG)

reg_lasso.score(x_test, y_test)

reg_ridge.score(x_test, y_test)
