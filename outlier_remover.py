import pandas as pd
import numpy as np
from scipy.stats import zscore
import openpyxl

# Load the uploaded data
file_path = 'cleaned_data.xlsx'

# Manually assign the correct column names based on the second row in the original file
column_names = ['conc', 'B', 'G', 'R', 'L', 'a', 'b', 'H', 'S', 'I']

# Load the data again, skipping the first two rows and assigning the correct column names
data = pd.read_excel(file_path, skiprows=2, names=column_names)

# Convert the columns to appropriate data types
dataset = data.apply(pd.to_numeric)

# Calculate Z-scores for each column
z_scores = np.abs(zscore(dataset))

# Set a threshold for the Z-score to identify outliers
threshold = 3

# Filter out the outliers
dataset_no_outliers = dataset[(z_scores < threshold).all(axis=1)]

# Save the updated dataset back to the Excel file
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    dataset_no_outliers.to_excel(writer, sheet_name='Sheet1', index=False)

print("Outliers removed and changes saved to the Excel file successfully.")
