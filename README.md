# Data Mining for Big Data Project - 2024

## Overview

Welcome to the Data Mining for Big Data Project repository. This project is part of the Master's program in Machine Learning and Data Mining at Jean Monnet University. Our team is focused on two-faceted tasks, aiming at both predicting the price of Bitcoin given a year of data containing multiple variables related to the Bitcoin blockchain and study the community structure of the network.

## Project Description - Task 1

## Project Description - Task 2

The primary challenge addressed in this task was doing the community analysis of a blockchain for an specific crypto-currency. It's important to mention that some of this tasks use PySpark, so it's mandatory to setup this tool in your machine before delving into the notebooks and codes on this section. The following guid shows how to setup this tool: https://spark.apache.org/docs/latest/api/python/getting_started/install.html

## Repository Contents
For this tasks the contents are the following:

- `bitcoin_price/`: General Bitcoin price analysis.
- `community_analysis/`: General Community analysis.
- `data/`: Data used for this task tokenized and not tokenized..
- `ego_analysis/`: General Ego analysis.
- `factor_analysis/`: General Factor analysis including: Estimated Output Volume, Exhange Trade Ratio and Monetary Velocity.
- `images/`: General images related to the Bitcoin price and the Ego analysis.

### Prerequisites

- See `requirements.txt` for a list of required Python packages for this specific task. Reminder: PySpark should be installed separately!

## Usage

In order to test a simple script of this section (monetary analysis), do the following steps:

1. We install the dependencies:

```
pip install -r requirements.txt
```
2. Move to the directory:

```
cd factor_analysis/
```
3. Execute Script:

```
python3 monetary_velocity.py
```

## Authors and Acknowledgment

- Made by Felipe CORTES JARAMILLO, Bastian SCHÄFER, Ariel GUERRA-ADAMES and Franck SIRGUEY.
- Supervised by Baptiste JEUDY and Christine LARGERON.