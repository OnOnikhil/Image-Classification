import openpyxl

# Load the workbook and select the active worksheet
file_path = 'cleaned_data.xlsx'  # Replace with your actual file path
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active  # Or use sheet name: workbook['Sheet1']

# Define the column to update (e.g., 'A' for the first column)
column_letter = 'B'

# Define the row after which you want to insert the value '250'
insert_after_row = 2002  # Replace with your desired row number
value = 25
# Insert '250' after the specified row
# Note: Adjust range as needed based on your Excel sheet structure
for row in range(insert_after_row + 2, 2508):  # Start from the row after insert_after_row
    sheet[f'{column_letter}{row}'].value = value

# Save the workbook
workbook.save(file_path)

print(f"Value {value} has been inserted after row {insert_after_row} in column {column_letter}.")
