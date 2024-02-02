import matplotlib.pyplot as plt

path1 = 'results_2015_Q1.txt'
path2 = 'results_2015_Q2.txt'
path3 = 'results_2015_Q3.txt'
path4 = 'results_2015_Q4.txt'
path5 = 'results_2016_Q1.txt'
path6 = 'results_2016_Q2.txt'
path7 = 'results_2016_Q3.txt'
path8 = 'results_2016_Q4.txt'
path9 = 'results_2017_Q1.txt'
path10 = 'results_2017_Q2.txt'

paths = [path1, path2, path3, path4, path5, path6, path7, path8, path9, path10]

neighbors = []
cliques = []
bridges = []
periphery = []

for file in paths:
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('Neighbors Avg: '):
                line = line.split('Neighbors Avg: ')[1]
                neighbors.append(float(line))
            elif line.startswith('Cliques Avg: '):
                line = line.split('Cliques Avg: ')[1]
                cliques.append(float(line))
            elif line.startswith('Brigdes Avg: '):
                line = line.split('Brigdes Avg: ')[1]
                bridges.append(float(line))
            elif line.startswith('Periphery Avg: '):
                line = line.split('Periphery Avg: ')[1]
                periphery.append(float(line))

bitcoin_values = [243.39, 257.66, 237.57, 430.05, 417.01, 607.37, 613.93, 997.69, 1079.75, 2499.98]
timestamp = ["2015 - Q1", "2015 - Q2", "2015 - Q3", "2015 - Q4", "2016 - Q1", "2016 - Q2", "2016 - Q3", "2016 - Q4", "2017 - Q1", "2017 - Q2"]
plt.figure(figsize=(10, 8))
plt.plot(timestamp, bitcoin_values, timestamp, neighbors, timestamp, cliques,  timestamp, bridges,  timestamp, periphery)
plt.xlabel("Timestamp")
plt.ylabel("Number of edges and nodes")
plt.yscale('log')
plt.legend(['Bitcoin Value in US-Dollar', 'Average Number of Neighbors', 'Average Number of Bridges', 'Average Number of Periphery Nodes'])
plt.show()