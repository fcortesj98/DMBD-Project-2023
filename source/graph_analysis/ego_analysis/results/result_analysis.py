import numpy as np

'''
Description: File to analyze the results of the ego network analysis.
Author: Basitan Shafer
Date: 2024-02-02
References: https://medium.com/orglens/enhancing-employee-social-capital-with-ego-network-analysis-4ff0fc6738e3
'''

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

for file in paths:
    neighbors = []
    cliques = []
    bridges = []
    periphery = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(' Number of Neighbors: '):
                line = line.split(' Number of Neighbors: ')[1]
                print(line)
                neighbors.append(int(line))
                print(neighbors)
            elif line.startswith(' Number of cliques: '):
                line = line.split(' Number of cliques: ')[1]
                cliques.append(int(line))
            elif line.startswith(' Number of Bridges: '):
                line = line.split(' Number of Bridges: ')[1]
                bridges.append(int(line))
            elif line.startswith(' Number of periphery nodes: '):
                line = line.split(' Number of periphery nodes: ')[1]
                periphery.append(int(line))
    neighbor_avg = np.average(neighbors, axis=0)
    cliques_avg = np.average(cliques, axis=0)
    bridges_avg = np.average(bridges, axis=0)
    periphery_avg = np.average(periphery, axis=0)
    with open(file, 'a') as j:
        j.write(("\n\nNeighbors Avg: " + str(neighbor_avg) + "\nCliques Avg: " + str(cliques_avg) + "\nBrigdes Avg: " + str(bridges_avg) + "\nPeriphery Avg: " + str(periphery_avg)))
