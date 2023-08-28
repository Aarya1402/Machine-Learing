# alternative to linear regression for more variables
# loss functions:
# 1.sum of sqared error
#  SSE = Σ(1 to n)(Yi- y`i)^2
# 2. mean of squared error
#  MSE = Σ(1 to n)(Yi- y`i)^2/n
# 3. absolute error
#  MAE = Σ(1 to n)|Yi- y`i|^2
# 4. cross entropy
# 5.hinge
# 6.huber
# 7.kullback-leibler
# givan an equation:
# find slop if slop >0 -> decrease by learning rate
#          if slop <0 -> increase by learing rate
# learning rate:
# New_x = x +- learning_rate*(dy/dx)
# learning rate should be small enough not to cross limit(-ve to +ve)
# why loss fuction and GD?
#   1.Exact methods computationally expensive
#   2.They  are direction of optimal solution
#   3.Fast enough to scale on big data
#   4.easy to understand and implement
# Gradient Descent:
# all datasets are used to compute loss
#   traing the model:
# feature---> model(prediction function)---->compute loss with lables(loss funtion)--->update parameters-->back to model
# data = x + y (training and test spliting)
# mini batch GD:
# Mini batches are used to copmute loss
# Stochastic gradient descent
# if batch size = 1 then SGD
