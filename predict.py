import pandas as pd 
from sklearn.linear_model import LinearRegression

data = pd.read_csv('train.csv',header=0)
# print(data.head())

#data[row range,column range]
x = data.iloc[ :  , 1:9  ]
y = data.iloc[ : , 11
              ]

print(x)

reg = LinearRegression().fit(x,y)