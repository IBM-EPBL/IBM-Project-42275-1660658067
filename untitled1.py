# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ANw1Nw4xR2TKoSv1-8BQpV78Lr11TGFq
"""

import numpy as np
import pandas as pd

df = pd.read_csv("Churn_Modelling.csv")

df

"""## 3.Visualizations"""

import matplotlib.pyplot as plt

import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

"""## ii)Bivariate Analysis"""

df[['CustomerId','Surname','CreditScore','Geography','Age','Tenure']].describe()

sns.histplot(df.Age,kde=True)

# plot count plot for the gender column
sns.countplot(df.Gender)

"""## ii)Bivariate Analysis"""

df[['CustomerId','Surname','CreditScore','Geography','Gender','Age']].corr()

sns.scatterplot(df.CreditScore,df.Age)
plt.ylim(0,100)

"""## iii)Multivariate Analysis"""

sns.pairplot(data =df[['CustomerId','Geography','Gender','CreditScore','Age','Balance']],hue = 'Balance')

"""## 6.Finding and replacing the outliers"""

#mode
df['Age'].mode()

#calculation of the mean (for Age)
df["Age"].mean()

#calculation of the mean and round the result(for Age)
round(df["Age"].mean(), 2)

#calculation of the median(for Age)
df["Age"].median()

df.columns

df["NumOfProducts"].value_counts()

df.dtypes

df.head()

df.describe()

df.isna().any()

df.isnull().sum()

df.isnull()

df.notnull()

"""
## 6.Finding and replacing the outliers"""

import seaborn as sns
sns.boxplot(x=df['Age'])

sns.boxplot(x=df['Tenure'])

"""## 7.Check for categorical columns and perform encoding"""

import pandas as pd
df = pd.read_csv("Churn_Modelling.csv", header=None)

cols = df.columns
num_cols = df._get_numeric_data().columns

num_cols

list(set(cols) - set(num_cols))

"""## 8.Split the data into dependent and independent variables"""

import pandas as pd
df = pd.read_csv("Churn_Modelling.csv", header=None)

# x  -Independent
# y  -Dependent
x =df.iloc[:,1:4].value_counts
print(x)

y=df.iloc[:,-1].value_counts
print(y)

"""## 9.Scale the independent variables"""

from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

import numpy as np
import pandas as pd
df = pd.read_csv("Churn_Modelling.csv")

X = df[['Balance', 'Tenure']]

scaledX = scale.fit_transform(X)

print(scaledX)

"""## 10.Split the data into training and testing"""

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

print('X Train shape:{},Y.Train SHape:{}'.format(x_train.shape,y_train.shape))

print('X Test Shape :{},Y Test SHape:{}'.format(x_test.shape,y_test.shape))