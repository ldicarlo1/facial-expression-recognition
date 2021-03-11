# DALT7012 - Assignment 1
# Data Visualization

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# read in data file
df = pd.read_csv("grammatical_facial_expression/a_affirmative_datapoints.txt",delimiter = " ",)

for i in range(len(df.columns)):
    print(i)


