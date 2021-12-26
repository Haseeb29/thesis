import pandas as pd
import numpy as np
import pickle, gzip
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
gtd = pd.read_csv("GTD_new.csv",encoding = "ISO-8859-1")
gtd['key'] = 0
NorthAmerica = gtd.loc[gtd['region'] == 1]
CentralAmerica = gtd.loc[gtd['region'] == 2 ]
SouthAmerica = gtd.loc[gtd['region'] == 3 ]
EastAsia = gtd.loc[gtd['region'] == 4 ]
SouthEastAsia = gtd.loc[gtd['region'] == 5 ]
SouthAsia = gtd.loc[gtd['region'] == 6 ]
CentralAsia = gtd.loc[gtd['region'] == 7 ]
WesternEurope = gtd.loc[gtd['region'] == 8 ]
EasternEurope = gtd.loc[gtd['region'] == 9 ]
MiddleEastNorthAfrica = gtd.loc[gtd['region'] == 10 ]
SubSaharanAfrica = gtd.loc[gtd['region'] == 11 ]
AustralasiaOceania = gtd.loc[gtd['region'] == 12 ]

def getRows(df,num):
  if len(df.index)>200:
    df = df.sample(n=num,replace=False)
  return df

def mergeDataframes(df1,df2):
  df_cartesian = df1.merge(df2, how='outer',on = 'key')
  return df_cartesian

# NorthAmerica = getRows(NorthAmerica,200)
# CentralAmerica = getRows(CentralAmerica,200)
# SouthAmerica = getRows(SouthAmerica,200)
# EastAsia = getRows(EastAsia,200)
# SouthEastAsia = getRows(SouthEastAsia,200)
# SouthAsia = getRows(SouthAsia,200)
# CentralAsia = getRows(CentralAsia,200)
# WesternEurope = getRows(WesternEurope,200)
# EasternEurope = getRows(EasternEurope,200)
# MiddleEastNorthAfrica = getRows(MiddleEastNorthAfrica,200)
# SubSaharanAfrica = getRows(SubSaharanAfrica,200)
# AustralasiaOceania = getRows(AustralasiaOceania,200)

# ## North-America Combinations
NA_CA = mergeDataframes(NorthAmerica,CentralAmerica)
mergedDF = NA_CA
del NA_CA
NA_SA = mergeDataframes(NorthAmerica,SouthAmerica)
mergedDF.append(NA_SA)
del NA_SA
NA_EAs = mergeDataframes(NorthAmerica,EastAsia)
mergedDF.append(NA_EAs)
del NA_EAs
NA_SEAs = mergeDataframes(NorthAmerica,SouthEastAsia)
mergedDF.append(NA_SEAs)
del NA_SEAs
NA_SAs = mergeDataframes(NorthAmerica,SouthAsia)
mergedDF.append(NA_SAs)
del NA_SAs
NA_CAs = mergeDataframes(NorthAmerica,CentralAsia)
mergedDF.append(NA_CAs)
del NA_CAs
NA_WEu = mergeDataframes(NorthAmerica,WesternEurope)
mergedDF.append(NA_WEu)
del NA_WEu
NA_EEu = mergeDataframes(NorthAmerica,EasternEurope)
mergedDF.append(NA_EEu)
del NA_EEu
NA_MENAf = mergeDataframes(NorthAmerica,MiddleEastNorthAfrica)
mergedDF.append(NA_MENAf)
del NA_MENAf
NA_SSAf = mergeDataframes(NorthAmerica,SubSaharanAfrica)
mergedDF.append(NA_SSAf)
del NA_SSAf
NA_AO = mergeDataframes(NorthAmerica,AustralasiaOceania)
mergedDF.append(NA_AO)
del NA_AO
# mergedDF = NA_CA
# arr = [NA_SA,NA_EAs,NA_SEAs,NA_SAs,NA_WEu,NA_EEu,NA_MENAf,NA_SSAf,NA_AO,NA_CAs]
# for x in arr:
#     mergedDF = mergedDF.append(x)
#     print(x.shape)
    
print('Central America Combination')
CA_SA = mergeDataframes(CentralAmerica,SouthAmerica)
mergedDF.append(CA_SA)
del CA_SA
CA_EAs = mergeDataframes(CentralAmerica,EastAsia)
mergedDF.append(CA_EAs)
del CA_EAs
CA_SEAs = mergeDataframes(CentralAmerica,SouthEastAsia)
mergedDF.append(CA_SEAs)
del CA_SEAs
CA_SAs = mergeDataframes(CentralAmerica,SouthAsia)
mergedDF.append(CA_SAs)
del CA_SAs
print('half')
CA_WEu = mergeDataframes(CentralAmerica,WesternEurope)
mergedDF.append(CA_WEu)
del CA_WEu
CA_EEu = mergeDataframes(CentralAmerica,EasternEurope)
mergedDF.append(CA_EEu)
del CA_EEu
CA_MENAf = mergeDataframes(CentralAmerica,MiddleEastNorthAfrica)
mergedDF.append(CA_MENAf)
del CA_MENAf
CA_SSAf = mergeDataframes(CentralAmerica,SubSaharanAfrica)
mergedDF.append(CA_SSAf)
del CA_SSAf
CA_AO = mergeDataframes(CentralAmerica,AustralasiaOceania)
mergedDF.append(CA_AO)
del CA_AO
exit()

# arr = [CA_SA,CA_EAs,CA_SEAs,CA_SAs,CA_WEu,CA_EEu,CA_MENAf,CA_SSAf,CA_AO]
# for x in arr:
#     mergedDF = mergedDF.append(x)
#     print(x.shape)
    
print('South America')

SA_EAs = mergeDataframes(SouthAmerica,EastAsia)
SA_SEAs = mergeDataframes(SouthAmerica,SouthEastAsia)
SA_SAs = mergeDataframes(SouthAmerica,SouthAsia)
SA_CAs = mergeDataframes(SouthAmerica,CentralAsia)
SA_WEu = mergeDataframes(SouthAmerica,WesternEurope)
SA_EEu = mergeDataframes(SouthAmerica,EasternEurope)
SA_MENAf = mergeDataframes(SouthAmerica,MiddleEastNorthAfrica)
SA_SSAf = mergeDataframes(SouthAmerica,SubSaharanAfrica)
SA_AO = mergeDataframes(SouthAmerica,AustralasiaOceania)
arr = [SA_EAs,SA_SEAs,SA_SAs,SA_WEu,SA_EEu,SA_MENAf,SA_SSAf,SA_AO,SA_CAs]
for x in arr:
    mergedDF = mergedDF.append(x)
    print(x.shape)
print('East Asia')
EAs_SEAs = mergeDataframes(EastAsia,SouthEastAsia)
EAs_SAs = mergeDataframes(EastAsia,SouthAsia)
EAs_CAs = mergeDataframes(EastAsia,CentralAsia)
EAs_WEu = mergeDataframes(EastAsia,WesternEurope)
EAs_EEu = mergeDataframes(EastAsia,EasternEurope)
EAs_MENAf = mergeDataframes(EastAsia,MiddleEastNorthAfrica)
EAs_SSAf = mergeDataframes(EastAsia,SubSaharanAfrica)
EAs_AO = mergeDataframes(EastAsia,AustralasiaOceania)
arr = [EAs_SEAs,EAs_SAs,EAs_CAs,EAs_WEu,EAs_EEu,EAs_MENAf,EAs_SSAf,EAs_AO]
for x in arr:
    mergedDF = mergedDF.append(x)
    print(x.shape)
print('South East Asia')
SEAs_SAs = mergeDataframes(SouthEastAsia,SouthAsia)
SEAs_CAs = mergeDataframes(SouthEastAsia,CentralAsia)
SEAs_WEu = mergeDataframes(SouthEastAsia,WesternEurope)
SEAs_EEu = mergeDataframes(SouthEastAsia,EasternEurope)
SEAs_MENAf = mergeDataframes(SouthEastAsia,MiddleEastNorthAfrica)
SEAs_SSAf = mergeDataframes(SouthEastAsia,SubSaharanAfrica)
SEAs_AO = mergeDataframes(SouthEastAsia,AustralasiaOceania)
arr = [SEAs_SAs,SEAs_CAs,SEAs_WEu,SEAs_EEu,SEAs_MENAf,SEAs_SSAf,SEAs_AO]
for x in arr:
    mergedDF = mergedDF.append(x)
    print(x.shape)
print('South Asia')
SAs_CAs = mergeDataframes(SouthAsia,CentralAsia)
SAs_WEu = mergeDataframes(SouthAsia,WesternEurope)
SAs_EEu = mergeDataframes(SouthAsia,EasternEurope)
SAs_MENAf = mergeDataframes(SouthAsia,MiddleEastNorthAfrica)
SAs_SSAf = mergeDataframes(SouthAsia,SubSaharanAfrica)
SAs_AO = mergeDataframes(SouthAsia,AustralasiaOceania)
arr = [SAs_CAs,SAs_WEu,SAs_EEu,SAs_MENAf,SAs_SSAf,SAs_AO]
for x in arr:
    mergedDF = mergedDF.append(x)
    print(x.shape)
print('Central Asia')
CAs_WEu = mergeDataframes(CentralAsia,WesternEurope)
CAs_EEu = mergeDataframes(CentralAsia,EasternEurope)
CAs_MENAf = mergeDataframes(CentralAsia,MiddleEastNorthAfrica)
CAs_SSAf = mergeDataframes(CentralAsia,SubSaharanAfrica)
CAs_AO = mergeDataframes(CentralAsia,AustralasiaOceania)
arr = [CAs_WEu,CAs_EEu,CAs_MENAf,CAs_SSAf,CAs_AO]
for x in arr:
    mergedDF = mergedDF.append(x)
    print(x.shape)
print('Western Europe')
WEu_EEu = mergeDataframes(WesternEurope,EasternEurope)
WEu_MENAf = mergeDataframes(WesternEurope,MiddleEastNorthAfrica)
WEu_SSAf = mergeDataframes(WesternEurope,SubSaharanAfrica)
WEu_AO = mergeDataframes(WesternEurope,AustralasiaOceania)
arr = [WEu_EEu,WEu_MENAf,WEu_SSAf,WEu_AO]
for x in arr:
    mergedDF = mergedDF.append(x)
    print(x.shape)
print('Eastern Europe')
EEu_MENAf = mergeDataframes(EasternEurope,MiddleEastNorthAfrica)
EEu_SSAf = mergeDataframes(EasternEurope,SubSaharanAfrica)
EEu_AO = mergeDataframes(EasternEurope,AustralasiaOceania)
arr = [EEu_MENAf,EEu_SSAf,EEu_AO]
for x in arr:
    mergedDF = mergedDF.append(x)
    print(x.shape)
print('MiddleEast North Africa')
MENAf_SSAf = mergeDataframes(MiddleEastNorthAfrica,SubSaharanAfrica)
MENAf_AO = mergeDataframes(MiddleEastNorthAfrica,AustralasiaOceania)
arr = [MENAf_SSAf,MENAf_AO]
for x in arr:
    mergedDF = mergedDF.append(x)
    print(x.shape)
print('Sub Saharan Africa')
SSAf_AO = mergeDataframes(SubSaharanAfrica,AustralasiaOceania)
arr = [SSAf_AO]
for x in arr:
    mergedDF = mergedDF.append(x)
    print(x.shape)
    
mergedDF['label'] = 0
print(mergedDF.columns)
mergedDF.loc[mergedDF['gname_x'] == mergedDF['gname_y'], 'label'] = 1
print(len(mergedDF[mergedDF.label == 1]))
print(len(mergedDF[mergedDF.label == 0]))
mergedDF.to_csv('out_final.csv', index=False)
print("done")
