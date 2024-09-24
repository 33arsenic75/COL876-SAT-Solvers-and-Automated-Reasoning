import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('benchmark_results.csv')

# Extract the serial number and r value from the file name
df['serial_number'] = df['test_file'].str.extract(r'3sat_r\d+\.\d+_(\d+)\.cnf')
df['r_value'] = df['test_file'].str.extract(r'3sat_r(\d+\.\d+)_\d+\.cnf')

# Convert serial_number to numeric
df['serial_number'] = pd.to_numeric(df['serial_number'])
df['r_value'] = pd.to_numeric(df['r_value'])

# Group by r value and calculate the mean of the time columns
time_columns = ['ordered_time', 'random_time', 'frequent_time', 'dynamic_time', 'jeroslow_time', 'vsids_time']
mean_times_by_r = df.groupby('r_value')[time_columns].mean()

# Plotting the mean times for each heuristic as per r value
plt.figure(figsize=(10, 6))
for column in time_columns:
    plt.plot(mean_times_by_r.index, mean_times_by_r[column], label=column)

plt.xlabel('r value')
plt.ylabel('Mean Time (s)')
plt.title('Mean Time Taken by Each Heuristic as per r Value')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('plot.png')

# Calculate the number of SAT values for each r value
sat_columns = ['ordered_satisfiability', 'random_satisfiability', 'frequent_satisfiability', 'dynamic_satisfiability', 'jeroslow_satisfiability', 'vsids_satisfiability']
df['sat_count'] = df[sat_columns].apply(lambda row: row.str.count('SAT').sum(), axis=1)
sat_counts = df.groupby('r_value')['sat_count'].sum()

# Calculate the mean time for each heuristic
mean_heuristic_times = df[time_columns].mean()

# Print the results
print("Mean times by r:")
print(mean_times_by_r)
print("\nSAT counts by r value:")
print(sat_counts)
print("\nMean times for each heuristic:")
print(mean_heuristic_times)
