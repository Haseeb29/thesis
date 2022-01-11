import pandas as pd
import numpy as np
gtd = pd.read_csv("out_final50.csv",encoding = "ISO-8859-1")
print(len(gtd[gtd.label == 1]))
print(len(gtd[gtd.label == 0]))