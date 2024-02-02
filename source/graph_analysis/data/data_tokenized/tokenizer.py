from pandas import read_csv
from pathlib import Path
import json

# Generate look-up dict with an identifying value for each key (Target / Source)
dict = {}

# read csv file
path1 = "../../../../../../schaefer.bastian/Documents/1. Studium/Master/3. Semester/Vorlesungen/Data Mining/Project/data/networks/"
path2 = "../../../../../../schaefer.bastian/Documents/1. Studium/Master/3. Semester/Vorlesungen/Data Mining/Project/data/networks_new/"

for child in Path(path1).iterdir():
    if child.is_file():
        df = read_csv(path1 + child.name)

        i = 0
        for index, name in df['Source'].items():
            if name not in dict:
                dict[name] = i
                i += 1
        for index, name in df['Target'].items():
            if name not in dict:
                dict[name] = i
                i += 1
        with open(path2 + 'dict.json', 'w') as json_file:
            json.dump(dict, json_file)

        df['Source'] = df['Source'].map(dict)
        df['Target'] = df['Target'].map(dict)

        df.to_csv(path2 + child.name)
