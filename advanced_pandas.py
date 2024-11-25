# -*- coding: utf-8 -*-
"""advanced_pandas.ipynb

"""

import pandas as pd
import numpy as np

#pandas(grouping, aggregation, merging)

from google.colab import files
uploaded = files.upload()

elections = pd.read_csv("elections.csv")
elections

elections.query("Year  >  1990  and Result=='win'").sort_values("%", ascending=False)

#candidate name lenrth sorting
elections.query("Year  >  1990  and Result=='win'").sort_values("Candidate", key=lambda x : x.str.len(), ascending=False)

#aggregation

max_candidate = max(elections.query("Result=='win'")["%"])

current_candidate =elections.query("Result=='win'")["%"].iloc[-1]
print(current_candidate)

RTP = current_candidate/max_candidate
print(RTP)

elections.groupby("Party").agg(sum)

