import pandas as pd

# Load the two CSV files into DataFrames
file1 = pd.read_csv('benchmark_results.csv')
file2 = pd.read_csv('benchmark_results_1.csv')

# Perform an outer merge to keep all rows, even if they're present in only one file
merged = pd.merge(file1, file2, on=['FileName', 'r'], how='outer')

# Fill missing values with the default values
# You can specify the default values for each column below
default_values = {
    'random_time': 1800, 'twoclause_time': 1800, 'random_satisfiability': 'TIMEOUT', 'twoclause_satisfiability': 'TIMEOUT',
    'random_decision': 5000, 'twoclause_decision':5000, 'dynamic_time': 'TIMEOUT', 'jeroslow_time': 'TIMEOUT',
    'dynamic_satisfiability': 'TIMEOUT', 'jeroslow_satisfiability': 'TIMEOUT', 'dynamic_decision': 'TIMEOUT', 'jeroslow_decision': 'TIMEOUT'
}

merged.fillna(value=default_values, inplace=True)

# Define the column order
column_order = [
    'r', 'FileName', 
    'random_decision', 'twoclause_decision', 'dynamic_decision', 'jeroslow_decision',  # Decision counts
    'random_satisfiability', 'twoclause_satisfiability', 'dynamic_satisfiability', 'jeroslow_satisfiability',  # Satisfiability
    'random_time', 'twoclause_time', 'dynamic_time', 'jeroslow_time'  # Time columns (optional, ordered at the end)
]

# Reorder the columns
merged = merged[column_order]

# Save the result to a new CSV file
merged.to_csv('merged.csv', index=False)

# Display the merged DataFrame (optional)
print(merged)