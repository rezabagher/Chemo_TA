# -*- coding: utf-8 -*-
"""fa1.ipynb

"""

#pandas assignmet answer

import pandas as pd

f1 = pd.Series([100,50,25,10,5])
f1

f1.head(2)

f1.tail(2)

f1.index=["a","b","c","d","f"]

f1

#function (def) assignment answer

def ajib(x):
  return x**2+5*x+5

ajib(5)+ajib(3)

#class assignment answer (emtiazi)
class Iran_Kodro:
  def __init__(self, price, model):
    self.price = price
    self.model = model
  def new_price(self):
    self.price = self.price+100
  def new_model(self, model_name):
    self.model.append(model_name)

iran_khodro = Iran_Kodro(222, ["pide"])
iran_khodro.new_model("samand")
iran_khodro.new_price()
iran_khodro.price

