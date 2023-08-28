# logistic regression is classifier
# calculates probability
# if prob is high then x lable
# probability can not be defined ny linear regression as 0<= prob<= 1
# sigmoid function: maps the value btw 0 and 1
# y = 1/(1+e^-x)
# x = ∞ => y = 1
# x = -∞ => y = 0
# linear reg: Y = WX + B = log(ohds) where ohds = (y`/1-y`)
# prob = y` = 1/(1+e^-Y)
# loss = -ylogy` if Y = 0
# loss = -(1-y)(log(1-y`)) if y = 0
# finally, loss(single value) = -ylogy`-(1-y)(log(1-y`))
# loss(all data) = -1/m Σ(1 to m)yi log y`i + (1-y)(log(1-y`i)) where m = no of datasets
# we will get weights and bias from loss
# and we will get y = wx+b


# Logistic regression is a reg algo which does classification
# calculates prob of belonging to a perticular class
# if prob> 50% ->1 else 0
# How logistic reg work?
#   Takes your features and lables
#   fits a linear model(weights and biases)
#   And instead of giving you result, it gives you the logistic of the result(btw 0 and 1)

# training a logistic regression classifier to predict whether a flower is iris-verginica or not
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
iris = datasets.load_iris()
# print(list(iris.keys()))
# # ['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module']
# print(iris['data'])
# print(iris['target'])
# # target        0 - Iris-Setosa
#                 # 1 - Iris-Versicolour
#                 # 2 - Iris-Virginica
# print(iris['DESCR'])

x = iris["data"][:, 3:]
y = (iris["target"] == 2).astype(np.int32)
# print(y)
clf = LogisticRegression()
clf.fit(x,y)
predict = clf.predict([[2.6]])# checks whether data is iris virginica or not
print(predict)# 0
# using matplotlib to plot the visulization
x_new = np.linspace(0,3,1000).reshape(-1,1)
print(x_new)
y_prob = clf.predict_proba(x_new)
plt.plot(x_new,y_prob[:,1],"g-")# Checks prob to be a iris virginica
plt.show()


