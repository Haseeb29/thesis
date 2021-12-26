import pandas as pd
import numpy as np
import pickle, gzip
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
gtd = pd.read_csv("out_final50.csv",encoding = "ISO-8859-1")
mergedDF = gtd.drop(columns='key')
mergedDF_x = mergedDF.drop(columns='label')
mergedDF_x = mergedDF_x.values
min_max_scaler = MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(mergedDF_x)
y = mergedDF['label'].values
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=0)
model1 = svm.SVC(C=5, kernel='rbf')
print("fitting")
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
model1.fit(x_train, y_train)
pred1 = model1.predict(x_test)
acc1 = np.mean(pred1==np.argmax(y_test, axis=1))*100
