# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: CSV Handling using Pandas – Read and Display Data
# -------------------------------------------------------------

import pandas as pd

# -------------------------------------------------------------
# Step 1: Read CSV file using pandas
# -------------------------------------------------------------
# read_csv() loads the CSV into a DataFrame

df = pd.read_csv("TD.csv")

# -------------------------------------------------------------
# Step 2: Print the DataFrame
# -------------------------------------------------------------
# Displays tabular data (rows & columns)

print(df)