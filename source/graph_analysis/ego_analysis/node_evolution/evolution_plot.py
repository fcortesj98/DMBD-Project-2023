import matplotlib.pyplot as plt

'''
Description: File to analyze the results of the ego network analysis.
Author: Basitan Shafer
Date: 2024-02-02
References: https://medium.com/orglens/enhancing-employee-social-capital-with-ego-network-analysis-4ff0fc6738e3
'''

# Your data
data = [
    [12, 762, 11, 2210, 0, 28, 270, 2, 2636, 278],
    [12, 11, 762, 2210, 28, 2, 0, 270, 278, 38],
    [12, 11, 0, 2210, 28, 762, 2, 270, 1, 278],
    [12, 0, 11, 762, 2, 2210, 1, 28, 365, 38],
    [12, 0, 2, 2210, 11, 762, 2183, 56, 1, 38],
    [0, 12, 2, 11, 2183, 2210, 188, 56, 1, 61],
    [0, 12, 2, 188, 11, 1, 2183, 56, 2210, 64],
    [0, 12, 2, 11, 188, 894, 56, 1, 2210, 374],
    [0, 894, 188, 12, 2, 56, 2210, 1, 374, 38],
    [0, 56, 894, 188, 1, 374, 2210, 2, 12, 984]
]

# Flatten the data to get a list of all entities across time periods
all_entities = [entity for time_period in data for entity in time_period]
# Count the occurrences of each entity
entity_counts = {entity: all_entities.count(entity) for entity in set(all_entities)}
# Extract entities and counts for plotting

sorted_entities = sorted(entity_counts.items(), key=lambda x: x[0], reverse=False)

entities, counts = zip(*sorted_entities)

list = [i for i in range(len(entities))]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(list, counts, color='skyblue', align='center')
plt.xlabel('Label of Node')
plt.ylabel('Number of Occurrences')
plt.title('Count of Occurrences of each Node across Time Periods')
plt.xticks(list, entities, rotation=90, ha='right')
plt.show()
