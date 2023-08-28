# refer KMP notes for regression


import matplotlib as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
diabates = datasets.load_diabetes()

print(diabates.keys())
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
print(diabates.data)
diabates_x = diabates.data[:, np.newaxis, 2]
print(diabates_x)
diabates_x_train = diabates_x[:-30]
diabates_x_test = diabates_x[-30:]

diabates_y_train = diabates.target[:-30]
diabates_y_test = diabates.target[-30:]

model = linear_model.LinearRegression()
model.fit(diabates_x_train, diabates_y_train)
diabates_y_pridected = model.predict(diabates_x_test)
print("Mean squared error is: ", mean_squared_error(
    diabates_y_test, diabates_y_pridected))  # loss function
print("Weight: ", model.coef_)
print("Intercept: ", model.intercept_)
plt.scatter(diabates_x_test, diabates_y_test)
plt.plot(diabates_x_test, diabates_y_pridected)
plt.show()
