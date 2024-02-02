import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

'''
Description: File to calculate the monetary velocity of Bitcoin transactions and visualize it alongside Bitcoin value and transaction metrics.
Author: Felipe Cortes Jaramillo
Date: 2024-02-02
References: https://cryptoeconomicsystems.pubpub.org/pub/pernice-cryptocurrencies-velocity/release/9
'''

# Paths to data
paths = [
    '../data/data_tokenized/2015-Q1/',
    '../data/data_tokenized/2015-Q2/',
    '../data/data_tokenized/2015-Q3/',
    '../data/data_tokenized/2015-Q4/',
    '../data/data_tokenized/2016-Q1/',
    '../data/data_tokenized/2016-Q2/',
    '../data/data_tokenized/2016-Q3/',
    '../data/data_tokenized/2016-Q4/',
    '../data/data_tokenized/2017-Q1/',
    '../data/data_tokenized/2017-Q2/',
]

# Consolidate data reading
df_list = [pd.concat((pd.read_csv(f) for f in glob.glob(os.path.join(path, "*.csv"))), ignore_index=True) for path in paths]

bitcoin_values = [243.39, 257.66, 237.57, 430.05, 417.01, 607.37, 613.93, 997.69, 1079.75, 2499.98]
timestamps = ["2015 - Q1", "2015 - Q2", "2015 - Q3", "2015 - Q4", "2016 - Q1", "2016 - Q2", "2016 - Q3", "2016 - Q4", "2017 - Q1", "2017 - Q2"]

# Initialize lists to store results
sums = []
nb_transactions = []
velocities = []

# Calculate totals and velocity
for i, (df, bitcoin_value) in enumerate(zip(df_list, bitcoin_values)):
    print(f"\n***** {timestamps[i]} *****")
    total_output = df['value'].sum()
    sums.append(total_output)
    total_nb_transaction = df['nb_transactions'].sum()
    nb_transactions.append(total_nb_transaction)
    
    # Assuming total holdings approximated by average Bitcoin value times total transactions
    velocity = total_output / (bitcoin_value * total_nb_transaction)
    velocities.append(velocity)
    
    print(f"Total Output: {total_output}")
    print(f"Total Number of Transactions: {total_nb_transaction}")
    print(f"Velocity: {velocity}")

# Visualization
plt.figure(figsize=(12, 8))
plt.title("Monetary Velocity alongside Bitcoin Value and Transaction Metrics")
plt.plot(timestamps, bitcoin_values, label='Bitcoin Value in US-Dollar', marker='o')
plt.plot(timestamps, sums, label='Sum of Transaction Values', linestyle='--')
plt.plot(timestamps, velocities, label='Monetary Velocity', marker='x')
plt.xlabel("Timestamp")
plt.yscale('log')
plt.legend()
plt.grid(True)

# Save the figure
save_path = './images/monetary_velocity_plot.png'
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
