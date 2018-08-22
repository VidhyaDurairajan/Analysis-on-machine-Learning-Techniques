#Preparing Data

from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

import numpy as np
import pandas as pd

df = pd.read_csv("E:/NJIT/Data Science/DataScience/DataScience-Python3/projects/Analysis on machine Learning Techniques/mammographic_masses.data.txt", na_values=['?'],names = ['BI_RADS','age','shape', 'margin', 'density','severity'])
df.head()

#Understanding the Data

df.describe()

# Extracting and Eliminating the data with NaN

df.loc[(df['age'].isnull())|
       (df['shape'].isnull())|
       (df['margin'].isnull())|
       (df['density'].isnull())]
       
df.dropna(inplace=True)
df.describe()

#Splitting data into Features and label

feature = df[['age','shape','margin','density']].values
feature_names=['age','shape','margin','density']
label = df['severity'].values
label

#Preprocessing : Normalizing data with standard Scaler

from sklearn import preprocessing

scaler = preprocessing.StandardScaler()
scaled_features = scaler.fit_transform(feature)
scaled_features

#  ANALYSIS 2: Support Vector Machine

# A Trail with SVC Linear Kernel

from sklearn import svm

C = 1.0
svc = svm.SVC(kernel='linear', C=C) 

#Accuracy obtained with SVM

from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(svc, scaled_features,label, cv=10)

cv_scores.mean()

# A Trial with SVC rbf Kernel

C = 1.0
svc = svm.SVC(kernel='rbf', C=C)
cv_scores = cross_val_score(svc, scaled_features,label, cv=10)
cv_scores.mean()

# A Trial with SVC sigmoid Kernel

C = 1.0
svc = svm.SVC(kernel='sigmoid', C=C)
cv_scores = cross_val_score(svc, scaled_features,label, cv=10)
cv_scores.mean()

# A Trial with SVC poly Kernel

C = 1.0
svc = svm.SVC(kernel='poly', C=C)
cv_scores = cross_val_score(svc, scaled_features,label, cv=10)
cv_scores.mean()