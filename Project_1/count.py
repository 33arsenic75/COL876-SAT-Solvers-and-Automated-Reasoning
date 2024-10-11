import pandas as pd

# Load the CSV files
benchmark_results = pd.read_csv('benchmark_results.csv')
benchmark_results_last = pd.read_csv('benchmark_results_last UIP Cut.csv')

# Load the additional CSV file
results = pd.read_csv('results.csv')

# Function to count SAT and UNSAT with a specified column name
def count_sat_unsat(df, column_name):
    counts = df.groupby('r')[column_name].value_counts().unstack(fill_value=0)
    return counts

# Count SAT and UNSAT for each file with the appropriate column names
counts_benchmark = count_sat_unsat(benchmark_results, 'jeroslow_satisfiability')  # For benchmark results
counts_last = count_sat_unsat(benchmark_results_last, 'jeroslow_satisfiability')  # For last benchmark results
counts_results = count_sat_unsat(results, 'Satisfiability')  # For results.csv

# Concatenate counts side by side with the previous counts
counts_combined = pd.concat([counts_benchmark, counts_last, counts_results], axis=1, keys=['benchmark_results', 'benchmark_results_last', 'results'])

# Display the combined results
print("\nCounts for all files side by side:")
print(counts_combined)  # This will print all columns of counts_combined
