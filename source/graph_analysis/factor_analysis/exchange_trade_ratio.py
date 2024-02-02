import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

'''
Description: File to calculate the exchange-trade-ratio of Bitcoin transactions and visualize it alongside Bitcoin value and transaction metrics.
Author: Basitan Shafer
Date: 2024-02-02
'''

# Read data
path1 = '../data/data_tokenized/2015-Q1/'
path2 = '../data/data_tokenized/2015-Q2/'
path3 = '../data/data_tokenized/2015-Q3/'
path4 = '../data/data_tokenized/2015-Q4/'
path5 = '../data/data_tokenized/2016-Q1/'
path6 = '../data/data_tokenized/2016-Q2/'
path7 = '../data/data_tokenized/2016-Q3/'
path8 = '../data/data_tokenized/2016-Q4/'
path9 = '../data/data_tokenized/2017-Q1/'
path10 = '../data/data_tokenized/2017-Q2/'

files_15_Q1 = glob.glob(os.path.join(path1, "*.csv"))
files_15_Q2 = glob.glob(os.path.join(path2, "*.csv"))
files_15_Q3 = glob.glob(os.path.join(path3, "*.csv"))
files_15_Q4 = glob.glob(os.path.join(path4, "*.csv"))
files_16_Q1 = glob.glob(os.path.join(path5, "*.csv"))
files_16_Q2 = glob.glob(os.path.join(path6, "*.csv"))
files_16_Q3 = glob.glob(os.path.join(path7, "*.csv"))
files_16_Q4 = glob.glob(os.path.join(path8, "*.csv"))
files_17_Q1 = glob.glob(os.path.join(path9, "*.csv"))
files_17_Q2 = glob.glob(os.path.join(path10, "*.csv"))

df_15_Q1 = pd.concat((pd.read_csv(f) for f in files_15_Q1), ignore_index=True)
df_15_Q2 = pd.concat((pd.read_csv(f) for f in files_15_Q2), ignore_index=True)
df_15_Q3 = pd.concat((pd.read_csv(f) for f in files_15_Q3), ignore_index=True)
df_15_Q4 = pd.concat((pd.read_csv(f) for f in files_15_Q4), ignore_index=True)
df_16_Q1 = pd.concat((pd.read_csv(f) for f in files_16_Q1), ignore_index=True)
df_16_Q2 = pd.concat((pd.read_csv(f) for f in files_16_Q2), ignore_index=True)
df_16_Q3 = pd.concat((pd.read_csv(f) for f in files_16_Q3), ignore_index=True)
df_16_Q4 = pd.concat((pd.read_csv(f) for f in files_16_Q4), ignore_index=True)
df_17_Q1 = pd.concat((pd.read_csv(f) for f in files_17_Q1), ignore_index=True)
df_17_Q2 = pd.concat((pd.read_csv(f) for f in files_17_Q2), ignore_index=True)

df_list = [df_15_Q1, df_15_Q2, df_15_Q3, df_15_Q4, df_16_Q1, df_16_Q2, df_16_Q3, df_16_Q4, df_17_Q1, df_17_Q2]

exchanges = []
trades = []

graph_name = "Error"
i = 0
for df in df_list:
    if i == 0:
        graph_name = "2015 - Q1"
    if i == 1:
        graph_name = "2015 - Q2"
    if i == 2:
        graph_name = "2015 - Q3"
    if i == 3:
        graph_name = "2015 - Q4"
    if i == 4:
        graph_name = "2016 - Q1"
    if i == 5:
        graph_name = "2016 - Q2"
    if i == 6:
        graph_name = "2016 - Q3"
    if i == 7:
        graph_name = "2016 - Q4"
    if i == 8:
        graph_name = "2017 - Q1"
    if i == 9:
        graph_name = "2017 - Q2"
    print("\n***** " + graph_name + " ***** ")
    i = i + 1
    total_output = df['value'].sum()
    exchanges.append(total_output)
    total_nb_transaction = df['nb_transactions'].sum()
    trades.append(total_nb_transaction)
    print(total_output)
    print(total_nb_transaction)

exchange_trade_ratio = []
for i in range(len(exchanges)):
    exchange_trade_ratio.append(exchanges[i] / trades[i])

bitcoin_values = [243.39, 257.66, 237.57, 430.05, 417.01, 607.37, 613.93, 997.69, 1079.75, 2499.98]
timestamp = ["2015 - Q1", "2015 - Q2", "2015 - Q3", "2015 - Q4", "2016 - Q1", "2016 - Q2", "2016 - Q3", "2016 - Q4", "2017 - Q1", "2017 - Q2"]
plt.figure(figsize=(10, 8))
plt.title("Comparison of the Sum and the Number of Transaction Values with the Bitcoin Price")
plt.plot(timestamp, bitcoin_values, timestamp, exchange_trade_ratio)
plt.xlabel("Timestamp")
plt.yscale('log')
plt.legend(['Bitcoin Value in US-Dollar', 'Exchange-Trade-Ratio'])
plt.grid()
plt.show()