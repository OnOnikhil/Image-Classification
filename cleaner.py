import pandas as pd
import openpyxl

# Load the uploaded data
file_path = 'cleaned_data.xlsx'

# Manually assign the correct column names based on the second row in the original file
column_names = ['conc', 'B', 'G', 'R', 'L', 'a', 'b', 'H', 'S', 'I']

# Load the data again, skipping the first two rows and assigning the correct column names
data = pd.read_excel(file_path, skiprows=2, names=column_names)

# Convert the columns to appropriate data types
dataset = data.apply(pd.to_numeric)

# Here you can apply any data transformations or modifications you need
# For example, let's say you want to multiply all feature columns by 2

# Select features and target variable
X = dataset.iloc[:, 1:]  # Features: all columns except the first one
y = dataset.iloc[:, 0]   # Target: the first column


# Combine the modified features back with the target
dataset_modified = pd.concat([y, X], axis=1)

# Save the updated dataset back to the Excel file
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    dataset_modified.to_excel(writer, sheet_name='Sheet1', index=False)

print("Modifications applied and saved to the Excel file successfully.")
