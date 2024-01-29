import pandas as pd
import json

# Load the Excel file
excel_file_path = 'myfile.xlsx'
df = pd.read_excel(excel_file_path)

# Drop empty rows and columns
df = df.dropna(how='all', axis=1).dropna(how='all', axis=0)

# Extract data and create JSON
json_data = {}
for index, row in df.iterrows():
    queue_name = row['Queue']
    for country_code in df.columns[1:]:
        value = row[country_code]
        if not pd.isna(value):
            key = f"{country_code}_{queue_name}"
            json_data[key] = round(float(value), 1)

# Save JSON to a file
json_file_path = 'output.json'
with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print(f"JSON data saved to {json_file_path}")
