import pandas as pd
import numpy as np
import pickle, gzip
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support, confusion_matrix
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
gtd = pd.read_csv("out_final50.csv",encoding = "ISO-8859-1")
mergedDF = gtd.drop(columns='key')
mergedDF_x = mergedDF.drop(columns='label')
mergedDF_x = mergedDF_x.values
min_max_scaler = MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(mergedDF_x)
y = mergedDF['label'].values
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.25, random_state=0)
model1 = svm.SVC(C=5, kernel='rbf')
print("SVM fitting")
model1.fit(x_train, y_train)
pred1 = model1.predict(x_test)
acc1 = accuracy_score(y_test,pred1)*100
metrics = precision_recall_fscore_support(y_test, pred1, average='micro')
print("SVM Accuracy",acc1)
print("SVM Precision",metrics[0])
print("SVM Recall",metrics[1])
print("SVM Fscore",metrics[2])
microF1 = f1_score(y_test, pred1, average='micro')
print("SVM MicroF1",microF1)
macroF1 = f1_score(y_test, pred1, average='macro')
print("SVM MacroF1",macroF1)
print("SVM confusion matrix",confusion_matrix(y_test, pred1))

model1 = svm.SVC(C=5, kernel='rbf')
print("Logistic fitting")
clf = LogisticRegression(random_state=0).fit(x_train, y_train)
pred1 = clf.predict(x_test)
acc2 = accuracy_score(y_test,pred1)*100
metrics2 = precision_recall_fscore_support(y_test, pred1, average='micro')
print("Logistic Accuracy",acc1)
print("Logistic Precision",metrics[0])
print("Logistic Recall",metrics[1])
print("Logistic Fscore",metrics[2])
microF1 = f1_score(y_test, pred1, average='micro')
print("Logistic MicroF1",microF1)
macroF1 = f1_score(y_test, pred1, average='macro')
print("Logistic MacroF1",macroF1)
print("Logistic confusion matrix",confusion_matrix(y_test, pred1))

