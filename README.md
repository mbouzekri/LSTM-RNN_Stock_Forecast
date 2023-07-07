# RNN-LSTM_Stock_Forecast
🤖 **LSTM Recurrent Neural Networks to Predict Stock Prices!**

This project aims to predict the opening stock price of any stock this LSTM has been trained on. <br />
In order to get accurate predictions, a training set of at least 5 years is recommended.<br />

We are only able to make predictions for extended amount of times because we already have the data for these periods. <br />
Browning motion makes future values of stock prices independent of the past, so it would be impossible to make such long term predictions otherwise.

I have included the results of the stock of Amazon (AMZN) and Google (GOOGL) as examples to demonstrate the. <br />
Note that the algorithm is learning at **time-step of 1**. <br />


# Instructions 
In order to get the forecast you are looking for, you first need to find a training dataset as well as testing dataset for the corresponing stock.<br />
This should be easily doable using Yahoo Finance. <br />

Make sure to change the datasets name to the following format "Name_Stock_Price_Train".csv for the training set and "Name_Stock_Price_Test".csv for the testing dataset.
Finally, change the stock_name variable to the corresponding stock, and run the main.py script. Included below and the resulting graphs for AMZN and GOOGL.


# GOOGL Forecast 04/2023:
<img width="583" alt="Screenshot 2023-07-07 at 10 48 22 AM" src="https://github.com/mbouzekri/RNN-LSTM_Stock_Forecast/assets/106405634/ee7219a4-6f61-4199-b69e-3545b6a3648f">

# GOOGL Forecast 2019-2023:
<img width="571" alt="Screenshot 2023-07-07 at 10 48 55 AM" src="https://github.com/mbouzekri/RNN-LSTM_Stock_Forecast/assets/106405634/ff513d31-f516-4e79-8e81-24a566154979">

# AMZN Forecast 06/2023:
<img width="590" alt="Screenshot 2023-07-07 at 10 43 21 AM" src="https://github.com/mbouzekri/RNN-LSTM_Stock_Forecast/assets/106405634/90ccf237-3c95-4cab-b966-c3c70534330c">

# AMZN Forecast 2019-2023:
<img width="583" alt="Screenshot 2023-07-07 at 10 44 23 AM" src="https://github.com/mbouzekri/RNN-LSTM_Stock_Forecast/assets/106405634/750dbe92-0602-45e9-a178-8fa92a9ef63c">
