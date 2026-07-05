import os
import kagglehub
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Download the dataset
path = kagglehub.dataset_download("velvetcrystal/student-productivity-dataset")

print("Dataset downloaded to:", path)

# Display all files in the dataset folder
print("\nFiles in the dataset:")
print(os.listdir(path))

# Find the CSV file automatically
csv_file = None
for file in os.listdir(path):
    if file.endswith(".csv"):
        csv_file = os.path.join(path, file)
        break

# Load the CSV file
if csv_file:
    df = pd.read_csv(csv_file)

    # Display all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    print("\nComplete DataFrame:\n")
    print(df)

    print("\nShape of the dataset:", df.shape)
else:
    print("No CSV file found in the downloaded dataset.")