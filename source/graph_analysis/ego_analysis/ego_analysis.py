import os
import glob
import datetime

# Data Wrangling
import pandas as pd

# Data Visualization´
import matplotlib.pyplot as plt

# Network Analysis
import networkx as nx
from tqdm import tqdm

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

Graphtype = nx.Graph()
# Use as normal Graph for Analysis
G_15_Q1 = nx.from_pandas_edgelist(df_15_Q1, 'Source', 'Target', ['value', 'nb_transactions'], create_using=nx.Graph)
G_15_Q2 = nx.from_pandas_edgelist(df_15_Q2, 'Source', 'Target', ['value', 'nb_transactions'], create_using=nx.Graph)
G_15_Q3 = nx.from_pandas_edgelist(df_15_Q3, 'Source', 'Target', ['value', 'nb_transactions'], create_using=nx.Graph)
G_15_Q4 = nx.from_pandas_edgelist(df_15_Q4, 'Source', 'Target', ['value', 'nb_transactions'], create_using=nx.Graph)
G_16_Q1 = nx.from_pandas_edgelist(df_16_Q1, 'Source', 'Target', ['value', 'nb_transactions'], create_using=nx.Graph)
G_16_Q2 = nx.from_pandas_edgelist(df_16_Q2, 'Source', 'Target', ['value', 'nb_transactions'], create_using=nx.Graph)
G_16_Q3 = nx.from_pandas_edgelist(df_16_Q3, 'Source', 'Target', ['value', 'nb_transactions'], create_using=nx.Graph)
G_16_Q4 = nx.from_pandas_edgelist(df_16_Q4, 'Source', 'Target', ['value', 'nb_transactions'], create_using=nx.Graph)
G_17_Q1 = nx.from_pandas_edgelist(df_17_Q1, 'Source', 'Target', ['value', 'nb_transactions'], create_using=nx.Graph)
G_17_Q2 = nx.from_pandas_edgelist(df_17_Q2, 'Source', 'Target', ['value', 'nb_transactions'], create_using=nx.Graph)

graph_list = [#G_15_Q1, G_15_Q2, G_15_Q3, G_15_Q4, G_16_Q1,
    G_16_Q2, G_16_Q3, G_16_Q4, G_17_Q1, G_17_Q2]

i = 0
graph_name = "Error"
with open('evolution_of_nodes.txt', 'w') as f:
    f.write(" ******************************************* \n Ego Analysis " + str(datetime.datetime.now()) + " \n ******************************************* ")
    for G in graph_list:
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
        print("\n\n ***** " + graph_name + " ***** ")
        f.write("\n\n\n ********  " + graph_name + " ******** ")
        i = i + 1
        print("i: " + str(i))
        # Calculate degree centrality for each node
        degree_centrality = nx.degree_centrality(G)
        # Sort nodes by degree centrality in descending order
        sorted_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)
        # Get the top 10 most connected nodes
        top_10_nodes = sorted_nodes[:10]
        print("Nodes: " + str(top_10_nodes))
        f.write("\nNodes: " + str(top_10_nodes))
        for node in top_10_nodes:
            print("\n *** Node " + str(node) + " ***")
            f.write("\n\n ***** Node " + str(node) + " *****")
            ego_G = nx.ego_graph(G, node, center=True)
            # Cliques
            number_of_cliques = nx.number_of_cliques(ego_G)
            print("Number of cliques: " + str(number_of_cliques))
            f.write("\n Number of cliques: " + str(number_of_cliques))
            ego_G.clear()