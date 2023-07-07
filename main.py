# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

# Importing Math to calculate Root Mean Square (RMSE)
import math
from sklearn.metrics import mean_squared_error

# Just predicting the "Open Stock Price" for the stock. So extracting 1 column.
stock_name = 'GOOGL'
training_set_raw = pd.read_csv(stock_name + '_Stock_Price_Train.csv')
training_set = training_set_raw.iloc[:,1:2].values

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
training_set = sc.fit_transform(training_set)

# Getting the inputs and the ouputs
# Restricting the input and output based on how LSTM functions.
X_train = training_set[0:-1]
y_train = training_set[1::]

# Reshaping - Adding time interval as a dimension for input.
X_train = np.reshape(X_train, (len(X_train), 1, 1))

# Initialising the RNN
# Creating an object of Sequential class to create the RNN.
regressor = Sequential()

# Adding the input layer and the LSTM layer
# 4 memory units, sigmoid activation function and (None time interval with 1 attribute as input)
regressor.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 1)))

# Adding the output layer
regressor.add(Dense(units = 1))

# Compiling the RNN
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
regressor.fit(X_train, y_train, batch_size = 32, epochs = 200)

# Getting the real stock price of the Test Period
test_set = pd.read_csv(stock_name + '_Stock_Price_Test.csv')
real_stock_price = test_set.iloc[:,1:2].values

# Getting the predicted stock price of the Test Period
inputs = real_stock_price
inputs = sc.transform(inputs)
inputs = np.reshape(inputs, (len(test_set), 1, 1))
predicted_stock_price = regressor.predict(inputs)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# Visualising the results
real_stock_price = test_set.iloc[:,1:2].values
dates = pd.to_datetime(test_set['Date'])
plt.plot(dates, real_stock_price, color = 'forestgreen', label = stock_name + ' Stock Price')
plt.plot(dates, predicted_stock_price, color = 'goldenrod', label = 'Predicted ' + stock_name + ' Stock Price')
plt.title('LSTM RNN Stock Price Prediction')
plt.xlabel('Time (Days)')
plt.ylabel('Stock Price ($)')
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Making predictions for the entire dataset
# Getting the real stock price of the Training Period
real_stock_price_train = pd.read_csv(stock_name + '_Stock_Price_Train.csv')
real_stock_price_train = real_stock_price_train.iloc[:,1:2].values

# Getting the predicted stock price of the Training Period
predicted_stock_price_train = regressor.predict(X_train)
predicted_stock_price_train = sc.inverse_transform(predicted_stock_price_train)

# Visualising the results
dates = pd.to_datetime(training_set_raw['Date'])
plt.plot(dates, real_stock_price_train, color = 'crimson', label = stock_name + ' Stock Price')
plt.plot(dates[1::], predicted_stock_price_train, color = 'navy', label = 'Predicted ' + stock_name + ' Stock Price')
plt.title('LSTM RNN Stock Price Prediction')
plt.xlabel('Time (Months)')
plt.ylabel('Stock Price ($)')
plt.legend()
plt.xticks(rotation = 45)
plt.show()

# Calculating the Root Mean Square (RMSE) to evaluate the RNN
rmse = math.sqrt(mean_squared_error(real_stock_price, predicted_stock_price))
print(rmse / np.mean(real_stock_price) * 100)
