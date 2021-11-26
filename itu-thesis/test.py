import pandas as pd
import numpy as np
import pickle, gzip
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
gtd = pd.read_csv("GTD.csv",encoding = "ISO-8859-1")
