# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZgrHwQjSI0ziHe2PXr4yLMfD-nUZmOxs
"""

import numpy as np
import pandas as pd
df = pd.read_csv("Churn_Modelling.csv")
df

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
df[['CustomerId','Surname','CreditScore','Geography','Age','Tenure']].describe()

sns.histplot(df.Age,kde=True)

# plot count plot for the gender column
sns.countplot(df.Gender)

df[['CustomerId','Surname','CreditScore','Geography','Gender','Age']].corr()

sns.scatterplot(df.CreditScore,df.Age)
plt.ylim(0,100)

sns.pairplot(data =df[['CustomerId','Geography','Gender','CreditScore','Age','Balance']],hue = 'Balance')

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

import seaborn as sns
sns.boxplot(x=df['Age'])

sns.boxplot(x=df['Tenure'])

import pandas as pd
df = pd.read_csv("Churn_Modelling.csv", header=None)
cols = df.columns
num_cols = df._get_numeric_data().columns
num_cols

list(set(cols) - set(num_cols))

# x - Independent
# y - Dependent
x=df.iloc[:,1:4].value_counts
print(x)

y=df.iloc[:,-1].value_counts
print(y)

from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

import numpy as np
import pandas as pd
df = pd.read_csv("Churn_Modelling.csv")

X = df[['Balance','Tenure']]

scaledX = scale.fit_transform(X)

print(scaledX)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

print('X Train shape:{},Y.Train SHape:{}'.format(x_train.shape,y_train.shape))

print('X Test Shape :{},Y Test SHape:{}'.format(x_test.shape,y_test.shape))