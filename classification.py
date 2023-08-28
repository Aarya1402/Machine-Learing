# classification vs regression
# classifiaction: lables are defined
# regression: lables are as variable
# decision boundry

# KNN : K Nearest Neighbours
# if (k = val) then max(nearest member) will be lable
# if nearest members are same then distance will be considered
# cons:
# burden on testing, finding k, complex computation ,slow on big data
# pros:
# easy to understand and implement

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
# loading datasets
iris = datasets.load_iris()
# print(iris.DESCR) description about iris dataset
features = iris.data
lables = iris.target
print(features[0], lables[0])
# training the classifier
clf = KNeighborsClassifier()
clf.fit(features, lables)
predict = clf.predict([[1, 1, 1, 1]])
print(predict)
